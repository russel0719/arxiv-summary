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
from groq import Groq, BadRequestError
from dotenv import load_dotenv

# ====================================================
# Setup
# ====================================================
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SCORE_MODEL_NAME = "openai/gpt-oss-20b"
REPORT_MODEL_NAME = "openai/gpt-oss-20b"

SCORE_CALL_INTERVAL = 5  # seconds
SUMMARY_CALL_INTERVAL = 20  # seconds
REPORT_CALL_INTERVAL = 60  # seconds

CATEGORIES = ["cs.AI", "cs.LG", "cs.CV", "cs.CL", "stat.ML"]

OUTPUT_DIR = "daily_reports"
PDF_DIR = "pdfs"

os.makedirs("logs", exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

TOP_K = 8

# ====================================================
# Keyword Sets (Balanced)
# ====================================================
CV_KEYWORDS = [
    "image", "vision", "object detection", "segmentation",
    "3d reconstruction", "point cloud", "depth estimation",
    "video understanding", "optical flow", "tracking",
    "vision transformer", "vit", "cnn",
    "diffusion", "image generation", "video generation",
]

NLP_KEYWORDS = [
    "language", "text", "language model", "llm",
    "transformer", "attention",
    "instruction tuning", "alignment",
    "retrieval", "rag", "question answering",
    "reasoning", "summarization",
]

ML_KEYWORDS = [
    "representation learning", "self-supervised", "contrastive",
    "foundation model", "multimodal", "vision-language",
    "agent", "reinforcement learning",
    "world model", "planning",
    "few-shot", "zero-shot",
]

NEGATIVE_KEYWORDS = [
    "survey", "review", "benchmark",
    "dataset", "challenge",
    "tutorial", "position paper",
]

POSITIVE_KEYWORDS = CV_KEYWORDS + NLP_KEYWORDS + ML_KEYWORDS

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
def call_llm(prompt, model_name, interval, max_tokens=10000, _retry=0):
    try:
        res = client.chat.completions.create(
            model=model_name,
            messages=[
                {"role": "system", "content": "You are a senior AI researcher."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.3,
            max_tokens=max_tokens,
        )
        time.sleep(interval)
        token_monitor.log_usage(res.usage.total_tokens)
        return res.choices[0].message.content
    except BadRequestError as e:
        if e.status_code == 413 and _retry < 3:
            truncated = prompt[:int(len(prompt) * 0.75)]
            print(f"⚠️ 413 Too Large — truncating prompt to 75% and retrying ({_retry + 1}/3)")
            return call_llm(truncated, model_name, interval, max_tokens, _retry + 1)
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

    while True:
        url = (
            f"http://export.arxiv.org/api/query?"
            f"search_query={query}&"
            f"sortBy=submittedDate&sortOrder=descending&"
            f"start={start}&max_results={batch_size}"
        )

        feed = feedparser.parse(url)
        if not feed.entries:
            break

        stop = False
        for e in feed.entries:
            # arXiv published timestamp (UTC)
            published_dt = datetime.strptime(
                e.published, "%Y-%m-%dT%H:%M:%SZ"
            ).replace(tzinfo=timezone.utc)

            if target_date <= published_dt < next_date:
                pdf_url = next(
                    (l.href for l in e.links if l.type == "application/pdf"), None
                )
                if pdf_url is None:
                    continue
                papers.append({
                    "id": e.id.split("/")[-1],
                    "title": e.title.replace("\n", " "),
                    "summary": e.summary,
                    "pdf_url": pdf_url,
                    "published": published_dt,
                })

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

    # JSON object fallback
    match = re.search(r"(\{\s*\".*?\"\s*\})", text, re.DOTALL)
    if match:
        return match.group(1)

    return None

def score_paper(paper):
    block = f"Title: {paper['title']}\nAbstract: {paper['summary']}"
    prompt = f"""
Evaluate the following AI research paper with brief reason.

Criteria:
- Novel algorithmic idea
- Technical depth
- Long-term research impact

Ignore:
- Surveys
- Datasets
- Benchmarks

Return ONLY valid JSON object, no explanation.

Format:
{{
  "score": float, "reason": str
}}

Papers:
{block}
"""

    raw = call_llm(prompt, SCORE_MODEL_NAME, SCORE_CALL_INTERVAL)
    json_text = extract_json(raw)

    if json_text is None:
        print("⚠️ JSON extraction failed, skipping batch")
        return {"score": 0.0, "reason": ""}

    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        print("⚠️ JSON parse error, skipping batch")
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
        partials.append(call_llm(prompt, REPORT_MODEL_NAME, SUMMARY_CALL_INTERVAL))

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
    raw = call_llm(final_prompt + "\n" + "\n".join(partials), REPORT_MODEL_NAME, SUMMARY_CALL_INTERVAL)
    json_text = extract_json(raw)
    
    if json_text is None:
        print("⚠️ JSON extraction failed, skipping paper")
        return {"main_idea": "", "key_contribution": "", "method_overview": "", "why_it_matters": ""}

    try:
        return json.loads(json_text)
    except json.JSONDecodeError:
        print("⚠️ JSON parse error, skipping paper")
        return {"main_idea": "", "key_contribution": "", "method_overview": "", "why_it_matters": ""}

# ====================================================
# Trend Synthesis
# ====================================================
def generate_trend_report(papers):
    merged = "\n\n".join(
        f"Title: {p['title']}\n{p['text_summary']}"
        for p in papers
    )

    prompt = f"""
Generate a daily AI research trend report in Korean.

Include:
1. Overall trend
2. CV-related themes
3. NLP-related themes
4. Cross-domain directions

Format in Markdown.
"""
    return call_llm(prompt + "\n" + merged, REPORT_MODEL_NAME, REPORT_CALL_INTERVAL)


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
        p["id"]: p for p in (cp or {}).get("summarized", [])
        if "text_summary" in p
    }

    token_monitor.init_monitoring("summarization")
    top_papers = sorted(scored, key=lambda x: x["score"], reverse=True)[:TOP_K]
    summarized = []
    for p in top_papers:
        if p["id"] in already_summarized:
            summarized.append(already_summarized[p["id"]])
            print(f"  ↩️  Skipping (cached): {p['title'][:60]}")
            continue
        pdf = download_pdf(p)
        text = load_pdf_text(pdf)
        summary = summarize_paper(text)
        p["text_summary"] = "\n".join([
            f"- Main Idea: {summary['main_idea']}",
            f"- Key Contribution: {summary['key_contribution']}",
            f"- Method Overview: {summary['method_overview']}",
            f"- Why It Matters: {summary['why_it_matters']}",
        ])
        p["final_summary"] = summary
        remove_pdf(p)
        summarized.append(p)
        save_checkpoint(target_str, "summarization", scored, summarized)
    top_papers = summarized
    print(f"📰 Summarization completed")

    token_monitor.init_monitoring("report_generation")
    report = generate_trend_report(top_papers)
    print(f"🗞️ Trend report generated")

    report += "\n\n## 개별 논문 요약\n\n"
    for p in top_papers:
        report += f"### {p['title']}\n"
        report += f"- Score: {p['score']}\n"
        report += f"- Reason: {p['reason']}\n"
        fs = p["final_summary"]
        report += (
            f"- Main Idea: {fs['main_idea']}\n"
            f"- Key Contribution: {fs['key_contribution']}\n"
            f"- Method Overview: {fs['method_overview']}\n"
            f"- Why It Matters: {fs['why_it_matters']}\n\n"
        )

    year_month_dir = os.path.join(
        OUTPUT_DIR, target.strftime("%Y"), target.strftime("%m")
    )
    os.makedirs(year_month_dir, exist_ok=True)

    date_str = target.strftime("%Y-%m-%d")
    out_path = os.path.join(year_month_dir, f"AI_Daily_Trend_{date_str}.md")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"✅ Report saved: {out_path}")

    update_readme(report, date_str, out_path)
    print(f"✅ README.md updated")

    clear_checkpoint(target_str)
    token_monitor.report()

# ====================================================
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Research Daily Trend Report Generator")
    parser.add_argument("--date", type=str, help="Target date in YYYYMMDD format")
    args = parser.parse_args()
    if args.date:
        run(args.date)
    else:
        run()
