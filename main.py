import os
import argparse
import time
import re
import json
import textwrap
import requests
import feedparser
import fitz
from datetime import datetime, timedelta, timezone
from google import genai
from google.genai import types
from dotenv import load_dotenv

# ====================================================
# Setup
# ====================================================
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

SCORE_MODEL_NAME = "gemini-3.1-flash-lite-preview"
REPORT_MODEL_NAME = "gemini-3.1-flash-lite-preview"
FALLBACK_MODEL_NAME = "gemini-2.5-flash-lite"

# Gemini free tier: conservative intervals to stay within rate limits
SCORE_CALL_INTERVAL = 6  # ~10 req/min (preview model free tier limit)
SUMMARY_CALL_INTERVAL = 6  # ~10 req/min per chunk
REPORT_CALL_INTERVAL = 10  # ~6 req/min for large outputs

CATEGORIES = ["cs.CV"]

OUTPUT_DIR = "daily_reports"
PDF_DIR = "pdfs"

os.makedirs("logs", exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

TOP_K = 10

# ====================================================
# Keyword Sets (CV-focused)
# ====================================================
CV_KEYWORDS = [
    # Core vision tasks
    "detection",
    "segmentation",
    "recognition",
    "classification",
    "tracking",
    "pose estimation",
    "depth estimation",
    "optical flow",
    "stereo",
    "3d reconstruction",
    "point cloud",
    "scene understanding",
    "semantic",
    "instance",
    # Generation & synthesis
    "image generation",
    "video generation",
    "image synthesis",
    "inpainting",
    "super-resolution",
    "style transfer",
    "diffusion",
    "gan",
    "vae",
    "nerf",
    "3d generation",
    # Architecture & methods
    "vision transformer",
    "vit",
    "convolution",
    "attention mechanism",
    "self-supervised",
    "contrastive learning",
    "few-shot",
    "zero-shot",
    "transfer learning",
    "multimodal",
    "vision-language",
    "visual grounding",
    # Applications
    "medical imaging",
    "autonomous driving",
    "action recognition",
    "video understanding",
    "face",
    "person re-identification",
    "anomaly detection",
    "remote sensing",
    "satellite",
]

NEGATIVE_KEYWORDS = [
    # Review / survey types
    "survey",
    "review",
    "overview",
    "systematic review",
    "meta-analysis",
    "tutorial",
    "position paper",
    # Data & eval
    "dataset",
    "benchmark",
    "challenge",
    "competition",
    "leaderboard",
    "annotation tool",
    # Non-research
    "technical report",
    "extended abstract",
    "workshop paper",
]

POSITIVE_KEYWORDS = CV_KEYWORDS


# ====================================================
# Token Usage Monitoring
# ====================================================
class TokenMonitor:
    def __init__(self):
        self.usages = {}
        self.current_name = None

    def init_monitoring(self, name):
        self.usages[name] = 0
        self.current_name = name

    def log_usage(self, tokens):
        if self.current_name is not None:
            self.usages[self.current_name] += tokens

    def reset(self):
        self.usages = {}
        self.current_name = None

    def report(self):
        for name, count in self.usages.items():
            print(f"💡 {name} - Tokens used: {count}")


token_monitor = TokenMonitor()


# ====================================================
# Rate-limit-safe LLM call
# ====================================================
def call_llm(prompt, model_name, interval, max_tokens=10000, _retry=0, _fallback=False):
    try:
        res = client.models.generate_content(
            model=model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                system_instruction="You are a senior AI researcher.",
                temperature=0.3,
                max_output_tokens=max_tokens,
            ),
        )
        time.sleep(interval)
        if res.usage_metadata:
            token_monitor.log_usage(res.usage_metadata.total_token_count or 0)
        return res.text
    except Exception as e:
        err_msg = str(e)
        # 요청이 너무 큰 경우 (413 또는 payload size 관련)
        if (
            "413" in err_msg
            or "too large" in err_msg.lower()
            or "payload" in err_msg.lower()
        ) and _retry < 3:
            truncated = prompt[: int(len(prompt) * 0.75)]
            print(
                f"⚠️ Payload Too Large — truncating prompt to 75% and retrying ({_retry + 1}/3)"
            )
            return call_llm(truncated, model_name, interval, max_tokens, _retry + 1)
        # 일일 한도 초과
        if "quota" in err_msg.lower() and (
            "day" in err_msg.lower() or "daily" in err_msg.lower()
        ):
            print(f"🚫 Daily quota exceeded — aborting")
            raise
        # 요청 속도 제한 (429)
        if "429" in err_msg or "rate" in err_msg.lower() or "quota" in err_msg.lower():
            if _retry < 5:
                wait = 60 * (_retry + 1)
                print(f"⚠️ Rate Limit — waiting {wait}s and retrying ({_retry + 1}/5)")
                time.sleep(wait)
                return call_llm(prompt, model_name, interval, max_tokens, _retry + 1)
        # 서버 과부하 (503) — fallback 모델로 전환
        if "503" in err_msg or "unavailable" in err_msg.lower():
            if not _fallback:
                print(
                    f"⚠️ Server Unavailable (503) — switching to fallback model: {FALLBACK_MODEL_NAME}"
                )
                return call_llm(
                    prompt,
                    FALLBACK_MODEL_NAME,
                    interval,
                    max_tokens,
                    _retry=0,
                    _fallback=True,
                )
        raise


# ====================================================
# Checkpoint
# ====================================================
def _checkpoint_path(target_str):
    return os.path.join("logs", f"checkpoint_{target_str}.json")


def save_checkpoint(target_str, stage, scored, summarized=None):
    def serialize(p):
        d = {k: v for k, v in p.items()}
        if isinstance(d.get("published"), datetime):
            d["published"] = d["published"].isoformat()
        return d

    data = {"stage": stage, "scored": [serialize(p) for p in scored]}
    if summarized is not None:
        data["summarized"] = [serialize(p) for p in summarized]
    with open(_checkpoint_path(target_str), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False)


def load_checkpoint(target_str):
    path = _checkpoint_path(target_str)
    if not os.path.exists(path):
        return None
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def clear_checkpoint(target_str):
    path = _checkpoint_path(target_str)
    if os.path.exists(path):
        os.remove(path)


# ====================================================
# Date Utilities
# ====================================================
def get_previous_business_day(ref: datetime):
    wd = ref.weekday()
    if wd == 0:
        return ref - timedelta(days=3)
    if wd in [5, 6]:
        return None
    return ref - timedelta(days=1)


# ====================================================
# arXiv Fetch (Pagination)
# ====================================================
def fetch_all_papers(target_date_str, batch_size=200):
    """
    Fetch all arXiv papers submitted on target_date (UTC),
    i.e. [target_date, target_date + 1 day)
    """
    query = "+OR+".join([f"cat:{c}" for c in CATEGORIES])
    start = 0
    papers = []

    # 날짜 범위 정의
    target_date = datetime.strptime(target_date_str, "%Y%m%d").replace(
        tzinfo=timezone.utc
    )
    next_date = target_date + timedelta(days=1)
    next_date_str = next_date.strftime("%Y%m%d")

    while True:
        url = (
            f"http://export.arxiv.org/api/query?"
            f"search_query={query}+AND+submittedDate:[{target_date_str}+TO+{next_date_str}]&"
            f"sortBy=submittedDate&sortOrder=descending&"
            f"start={start}&max_results={batch_size}"
        )

        feed = feedparser.parse(url)
        if not feed.entries:
            break

        stop = False
        for e in feed.entries:
            # arXiv published timestamp (UTC)
            published_dt = datetime.strptime(e.published, "%Y-%m-%dT%H:%M:%SZ").replace(
                tzinfo=timezone.utc
            )

            if target_date <= published_dt < next_date:
                pdf_url = next(
                    (l.href for l in e.links if l.type == "application/pdf"), None
                )
                if pdf_url is None:
                    continue
                papers.append(
                    {
                        "id": e.id.split("/")[-1],
                        "title": e.title.replace("\n", " "),
                        "summary": e.summary,
                        "pdf_url": pdf_url,
                        "published": published_dt,
                    }
                )

            elif published_dt < target_date:
                stop = True
                break

        if stop:
            break

        start += batch_size

    return papers


# ====================================================
# Cheap Keyword Filter
# ====================================================
def cheap_filter(papers):
    out = []
    for p in papers:
        text = (p["title"] + " " + p["summary"]).lower()
        if any(nk in text for nk in NEGATIVE_KEYWORDS):
            continue
        if any(pk in text for pk in POSITIVE_KEYWORDS):
            out.append(p)
    return out


# ====================================================
# Batch Scoring
# ====================================================
def extract_json(text: str):
    """
    LLM 출력에서 JSON array/object만 안전하게 추출
    """
    if not text:
        return None

    # ```json ... ``` 제거
    text = re.sub(r"```json|```", "", text).strip()

    # JSON array 우선
    match = re.search(r"(\[\s*{.*?}\s*\])", text, re.DOTALL)
    if match:
        return match.group(1)

    # JSON object fallback (greedy: 중첩 배열 포함 전체 object 추출)
    match = re.search(r"(\{.*\})", text, re.DOTALL)
    if match:
        return match.group(1)

    return None


def repair_json(text: str) -> str:
    """LLM이 자주 출력하는 비표준 JSON 패턴을 수정"""
    # Python 리터럴 → JSON 표준
    text = (
        text.replace("None", "null").replace("True", "true").replace("False", "false")
    )
    # trailing comma before } or ]
    text = re.sub(r",\s*([}\]])", r"\1", text)
    return text


def score_paper(paper):
    block = f"Title: {paper['title']}\nAbstract: {paper['summary']}"
    prompt = f"""
You are a senior computer vision researcher. Evaluate the following CV paper and assign a score from 0.0 to 10.0.

Scoring criteria (all must apply for a high score):
1. Novel algorithmic or architectural contribution to computer vision
2. Technical depth — concrete method, not just an application or analysis
3. Long-term research impact on CV tasks (detection, segmentation, generation, 3D, etc.)

Penalize heavily (score <= 4.0) if the paper is:
- A survey, review, or overview
- A new dataset or benchmark paper (primary contribution is data collection)
- A position paper, tutorial, or workshop summary
- A pure application paper with no new CV method
- A minor incremental improvement

Return ONLY valid JSON object, no explanation.

Format:
{{
  "score": float, "reason": str
}}

Paper:
{block}
"""

    raw = call_llm(prompt, SCORE_MODEL_NAME, SCORE_CALL_INTERVAL, max_tokens=400)
    json_text = extract_json(raw)

    if json_text is None:
        print(f"⚠️ JSON extraction failed, skipping paper (raw: {raw[:200]!r})")
        return {"score": 0.0, "reason": ""}

    try:
        return json.loads(repair_json(json_text))
    except json.JSONDecodeError:
        print(f"⚠️ JSON parse error, skipping paper (extracted: {json_text[:200]!r})")
        return {"score": 0.0, "reason": ""}


# ====================================================
# PDF Processing
# ====================================================
def download_pdf(p):
    path = os.path.join(PDF_DIR, f"{p['id']}.pdf")
    if not os.path.exists(path):
        r = requests.get(p["pdf_url"])
        with open(path, "wb") as f:
            f.write(r.content)
    return path


def remove_pdf(p):
    path = os.path.join(PDF_DIR, f"{p['id']}.pdf")
    if os.path.exists(path):
        os.remove(path)


def load_pdf_text(path):
    doc = fitz.open(path)
    return "\n".join(page.get_text() for page in doc)


def chunk_text(text, size=2000):
    return textwrap.wrap(text, size)


def summarize_paper(text):
    chunks = chunk_text(text)
    chunks = chunks[:3] + chunks[5:7]  # Intro + Method only

    partials = []
    for c in chunks:
        prompt = f"""
Summarize this section focusing on method and contribution.

Text:
{c}
"""
        partials.append(
            call_llm(prompt, REPORT_MODEL_NAME, SUMMARY_CALL_INTERVAL, max_tokens=1000)
        )

    final_prompt = f"""
Create a concise research summary in Korean including following subjects.
- Main idea
- Key contribution
- Method overview
- Why it matters

Return ONLY valid JSON object, no explanation.

Format:
{{
  "main_idea": str, "key_contribution": str, "method_overview": str, "why_it_matters": str
}}
"""
    raw = call_llm(
        final_prompt + "\n" + "\n".join(partials),
        REPORT_MODEL_NAME,
        SUMMARY_CALL_INTERVAL,
        max_tokens=800,
    )
    json_text = extract_json(raw)

    if json_text is None:
        print(f"⚠️ Summary JSON extraction failed (raw: {raw[:200]!r})")
        return {
            "main_idea": "",
            "key_contribution": "",
            "method_overview": "",
            "why_it_matters": "",
        }

    try:
        return json.loads(repair_json(json_text))
    except json.JSONDecodeError:
        print(f"⚠️ Summary JSON parse error (extracted: {json_text[:200]!r})")
        return {
            "main_idea": "",
            "key_contribution": "",
            "method_overview": "",
            "why_it_matters": "",
        }


# ====================================================
# Trend Synthesis
# ====================================================
TREND_JSON_SCHEMA = """\
{
  "overall_trends":      [{"field": str, "key_issue": str, "representative_paper": str}],
  "task_classification": [{"task": str, "key_content": str, "representative_paper": str}],
  "methodology_trends":  [{"methodology": str, "application_case": str, "representative_paper": str}],
  "cross_domain":        [{"fusion_field": str, "key_point": str, "expected_effect": str}],
  "headline": str
}"""


def generate_trend_report(papers) -> dict:
    merged = "\n\n".join(f"Title: {p['title']}\n{p['text_summary']}" for p in papers)
    prompt = f"""
You are a senior computer vision researcher.
Analyze today's top CV papers and extract structured trend information in Korean.

Return ONLY a valid JSON object, no explanation, no markdown fences.

JSON Schema:
{TREND_JSON_SCHEMA}

Field descriptions:
- overall_trends: 오늘 논문 전체의 연구 흐름을 분야별로 정리 (3~5개 행)
- task_classification: detection/segmentation/generation/3D/video/medical 등 CV 태스크별 분류 (등장한 태스크만 포함)
- methodology_trends: 오늘 논문에서 두드러진 아키텍처·학습 방법 (transformer, diffusion, self-supervised 등)
- cross_domain: CV와 다른 분야(의료, 자율주행, 로보틱스 등)의 융합 포인트 (없으면 빈 배열)
- headline: 오늘 CV 연구 전체를 한 문장으로 요약

Papers:
{merged}
"""
    raw = call_llm(prompt, REPORT_MODEL_NAME, REPORT_CALL_INTERVAL, max_tokens=3000)
    empty = {
        "overall_trends": [],
        "task_classification": [],
        "methodology_trends": [],
        "cross_domain": [],
        "headline": "",
    }
    # 트렌드 응답은 반드시 object여야 함 — array 우선 추출을 피하고 object만 파싱
    if raw:
        text = re.sub(r"```json|```", "", raw).strip()
        match = re.search(r"(\{.*\})", text, re.DOTALL)
        json_text = match.group(1) if match else None
    else:
        json_text = None
    if json_text is None:
        print(
            f"⚠️ Trend JSON extraction failed — using empty structure (raw: {raw[:200]!r})"
        )
        return empty
    try:
        result = json.loads(repair_json(json_text))
        if not isinstance(result, dict):
            print(
                f"⚠️ Trend JSON is not an object — using empty structure (type: {type(result).__name__})"
            )
            return empty
        return result
    except json.JSONDecodeError:
        print(
            f"⚠️ Trend JSON parse error — using empty structure (extracted: {json_text[:200]!r})"
        )
        return empty


def assemble_report(trend: dict, top_papers: list, date_str: str) -> str:
    def table_row(*cells):
        return "| " + " | ".join(str(c) for c in cells) + " |"

    lines = [f"# CV 연구 동향 보고서 — {date_str}\n"]

    # 1. 전체 트렌드
    lines += [
        "## 1. 전체 트렌드\n",
        table_row("분야", "핵심 이슈", "대표 논문"),
        table_row("------", "---------", "---------"),
    ]
    for r in trend.get("overall_trends", []):
        lines.append(
            table_row(
                r.get("field", ""),
                r.get("key_issue", ""),
                r.get("representative_paper", ""),
            )
        )
    if trend.get("headline"):
        lines.append(f"\n> 핵심 메시지: {trend['headline']}\n")

    # 2. CV 태스크별 분류
    lines += [
        "\n## 2. CV 태스크별 분류\n",
        table_row("태스크", "핵심 내용", "대표 논문"),
        table_row("------", "---------", "---------"),
    ]
    for r in trend.get("task_classification", []):
        lines.append(
            table_row(
                r.get("task", ""),
                r.get("key_content", ""),
                r.get("representative_paper", ""),
            )
        )

    # 3. 방법론 트렌드
    lines += [
        "\n## 3. 방법론 트렌드\n",
        table_row("방법론", "적용 사례", "대표 논문"),
        table_row("------", "---------", "---------"),
    ]
    for r in trend.get("methodology_trends", []):
        lines.append(
            table_row(
                r.get("methodology", ""),
                r.get("application_case", ""),
                r.get("representative_paper", ""),
            )
        )

    # 4. 크로스 도메인 융합
    lines += [
        "\n## 4. 크로스 도메인 융합\n",
        table_row("융합 분야", "핵심 포인트", "기대 효과"),
        table_row("---------", "-----------", "---------"),
    ]
    for r in trend.get("cross_domain", []):
        lines.append(
            table_row(
                r.get("fusion_field", ""),
                r.get("key_point", ""),
                r.get("expected_effect", ""),
            )
        )

    lines.append("\n---\n")

    # 5. 개별 논문 요약
    lines.append("## 5. 개별 논문 요약\n")
    for idx, p in enumerate(top_papers, start=1):
        arxiv_id = p["id"].split("v")[0]
        fs = p["final_summary"]
        lines += [
            f"### {idx}. {p['title']}\n",
            f"- **arXiv**: https://arxiv.org/abs/{arxiv_id}",
            f"- **Score**: {p['score']} / 10",
            f"- **한줄 요약**: {fs['main_idea']}",
            f"- **핵심 기여**: {fs['key_contribution']}",
            f"- **방법론 개요**: {fs['method_overview']}",
            f"- **의의**: {fs['why_it_matters']}\n",
        ]

    return "\n".join(lines)


def update_readme(report: str, date_str: str, report_path: str):
    readme_content = (
        "# arxiv-summary — AI Daily Trend\n\n"
        f"> 최신 보고서: **{date_str}** | "
        f"[원본 파일]({report_path}) | "
        "[전체 목록](daily_reports/) | "
        "[프로젝트 문서](DOCS.md)\n\n"
        "---\n\n"
        f"{report}\n"
    )
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme_content)


# ====================================================
# Main Pipeline
# ====================================================
def run(date: str = None):
    if date is not None:
        target = datetime.strptime(date, "%Y%m%d")
    else:
        now = datetime.now(timezone.utc)
        target = get_previous_business_day(now)
    if target is None:
        print("⏭️ Weekend – skipping")
        return

    target_str = target.strftime("%Y%m%d")
    print(f"📅 Target date: {target_str}")

    cp = load_checkpoint(target_str)

    # ── Scoring stage ──────────────────────────────
    if cp and cp["stage"] in ("summarization",):
        scored = cp["scored"]
        print(f"📂 Checkpoint restored: {len(scored)} scored papers")
    else:
        papers = fetch_all_papers(target_str)
        print(f"📄 Total fetched: {len(papers)}")
        if len(papers) == 0:
            print("⏭️ No papers found - skipping")
            return

        papers = cheap_filter(papers)
        print(f"🔎 After cheap filter: {len(papers)}")

        already_scored = {p["id"]: p for p in (cp or {}).get("scored", [])}

        token_monitor.init_monitoring("scoring")
        scored = list(already_scored.values())
        for paper in papers:
            if paper["id"] in already_scored:
                continue
            result = score_paper(paper)
            if result is not None:
                paper["score"] = result["score"]
                paper["reason"] = result["reason"]
                scored.append(paper)
                save_checkpoint(target_str, "scoring", scored)
        print(f"📝 Scoring completed")

    # ── Summarization stage ────────────────────────
    already_summarized = {
        p["id"]: p for p in (cp or {}).get("summarized", []) if "text_summary" in p
    }

    token_monitor.init_monitoring("summarization")
    # 점수가 낮은 논문(survey/dataset 등으로 판단된 것) 제외 후 상위 TOP_K 선택
    qualified = [p for p in scored if p.get("score", 0) >= 5.0]
    top_papers = sorted(qualified, key=lambda x: x["score"], reverse=True)[:TOP_K]
    print(
        f"🏆 Qualified papers (score >= 5.0): {len(qualified)}, selecting top {len(top_papers)}"
    )
    summarized = []
    for p in top_papers:
        if p["id"] in already_summarized:
            summarized.append(already_summarized[p["id"]])
            print(f"  ↩️  Skipping (cached): {p['title'][:60]}")
            continue
        pdf = download_pdf(p)
        text = load_pdf_text(pdf)
        summary = summarize_paper(text)
        p["text_summary"] = "\n".join(
            [
                f"- Main Idea: {summary['main_idea']}",
                f"- Key Contribution: {summary['key_contribution']}",
                f"- Method Overview: {summary['method_overview']}",
                f"- Why It Matters: {summary['why_it_matters']}",
            ]
        )
        p["final_summary"] = summary
        remove_pdf(p)
        summarized.append(p)
        save_checkpoint(target_str, "summarization", scored, summarized)
    top_papers = summarized
    print(f"📰 Summarization completed")

    token_monitor.init_monitoring("report_generation")
    trend_data = generate_trend_report(top_papers)
    print(f"🗞️ Trend report generated")

    date_str = target.strftime("%Y-%m-%d")
    report = assemble_report(trend_data, top_papers, date_str)

    year_month_dir = os.path.join(
        OUTPUT_DIR, target.strftime("%Y"), target.strftime("%m")
    )
    os.makedirs(year_month_dir, exist_ok=True)
    out_path = os.path.join(year_month_dir, f"CV_Daily_Trend_{date_str}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✅ Report saved: {out_path}")

    update_readme(report, date_str, out_path)
    print(f"✅ README.md updated")

    clear_checkpoint(target_str)
    token_monitor.report()


# ====================================================
# From-Selection Mode
# ====================================================
def run_from_selection(selection_file="selected_papers.json"):
    with open(selection_file, encoding="utf-8") as f:
        data = json.load(f)

    target = datetime.strptime(data["date"], "%Y-%m-%d")
    target_str = target.strftime("%Y%m%d")
    scored = data["papers"]
    print(f"📅 From selection: {data['date']}, {len(scored)} papers")

    cp = load_checkpoint(target_str)
    already_summarized = {
        p["id"]: p for p in (cp or {}).get("summarized", []) if "text_summary" in p
    }

    token_monitor.init_monitoring("summarization")
    qualified = [p for p in scored if p.get("score", 0) >= 5.0]
    top_papers = sorted(qualified, key=lambda x: x["score"], reverse=True)[:TOP_K]
    print(f"🏆 Selected papers: {len(top_papers)}")

    summarized = []
    for p in top_papers:
        if p["id"] in already_summarized:
            summarized.append(already_summarized[p["id"]])
            print(f"  ↩️  Skipping (cached): {p['title'][:60]}")
            continue
        pdf = download_pdf(p)
        text = load_pdf_text(pdf)
        summary = summarize_paper(text)
        p["text_summary"] = "\n".join(
            [
                f"- Main Idea: {summary['main_idea']}",
                f"- Key Contribution: {summary['key_contribution']}",
                f"- Method Overview: {summary['method_overview']}",
                f"- Why It Matters: {summary['why_it_matters']}",
            ]
        )
        p["final_summary"] = summary
        remove_pdf(p)
        summarized.append(p)
        save_checkpoint(target_str, "summarization", scored, summarized)

    top_papers = summarized
    print(f"📰 Summarization completed")

    token_monitor.init_monitoring("report_generation")
    trend_data = generate_trend_report(top_papers)

    date_str = target.strftime("%Y-%m-%d")
    report = assemble_report(trend_data, top_papers, date_str)

    year_month_dir = os.path.join(
        OUTPUT_DIR, target.strftime("%Y"), target.strftime("%m")
    )
    os.makedirs(year_month_dir, exist_ok=True)
    out_path = os.path.join(year_month_dir, f"CV_Daily_Trend_{date_str}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✅ Report saved: {out_path}")
    update_readme(report, date_str, out_path)
    print(f"✅ README.md updated")
    clear_checkpoint(target_str)
    token_monitor.report()


# ====================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="AI Research Daily Trend Report Generator"
    )
    parser.add_argument("--date", type=str, help="Target date in YYYYMMDD format")
    parser.add_argument(
        "--from-selection",
        type=str,
        nargs="?",
        const="selected_papers.json",
        metavar="FILE",
        help="Run from pre-selected papers JSON file",
    )
    args = parser.parse_args()

    if args.from_selection:
        run_from_selection(args.from_selection)
    elif args.date:
        run(args.date)
    else:
        run()
