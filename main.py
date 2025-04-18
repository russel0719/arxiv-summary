from langchain_perplexity import ChatPerplexity
from langchain_core.messages import HumanMessage, SystemMessage

import os
import re
import arxiv
from typing import List
from datetime import datetime
from docx import Document

PPLX_API_KEY = os.getenv("PPLX_API_KEY")
EXCEPT_KEYWORDS = ["robot", "security", "cripto", "emotion", "study", "report", "survey", "review"]
BATCH_SIZE = 25

client = arxiv.Client()
DOCUMENT_PATH = os.path.join(os.path.dirname(__file__), "{section}.docx")

    
def get_papers(section: str, last_submitted_date: str=None, max_results: int=BATCH_SIZE) -> List[arxiv.Result]:
    last_submitted_date = str(int(last_submitted_date) + 1) if last_submitted_date else None
    now = datetime.now().strftime("%Y%m%d%H%M")
    except_query = " OR ".join([f"ti:{keyword}" for keyword in EXCEPT_KEYWORDS])
    default_query = f"cat:{section} AND submittedDate:[{last_submitted_date} TO {now}]" if last_submitted_date else f"cat:{section}"
    search = arxiv.Search(
        query=f"{default_query} ANDNOT ({except_query})",
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Ascending,
    )
    results = list(client.results(search))
    print(f"Found {len(results)} papers in {section} section")
    return results


def get_summary_from_abstract(papers: List[arxiv.Result]) -> List[dict]:
    summaries = []
    for paper in papers:
        summary = {"title": paper.title, "url":paper.entry_id, "summary": paper.summary, "submitted_date": paper.published}
        summaries.append(summary)
    return summaries


def add_translations(llm: ChatPerplexity, summaries: List[dict]) -> List[dict]:
    formatted_abstracts = []
    for idx, s in enumerate(summaries, start=1):
        formatted_abstracts.append(f"{idx}. {s['summary'].strip().replace('\n', ' ')}")

    prompt = (
        "You will receive a numbered list of paper abstracts. Provide korean summary for each of the abstracts of all papers. Each summary should be written in 5 sentences\n"
        "Return the result in the format:\n\n"
        "1. <요약>\n2. <요약>\n...\n"
        "Do not skip any number. Only output the translations. Do not write in markdown format."
    )

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content="\n".join(formatted_abstracts))
    ]

    ai_message = llm.invoke(messages)
    print(ai_message.content)
    print("Bulk Translations Received.")

    # 파싱: "1. 번역내용" 형식에서 번호를 기준으로 split
    translations = re.findall(r"\d+\.\s+(.*?)(?=\n\d+\.|\Z)", ai_message.content.strip(), re.DOTALL)
    translations = [t.strip().replace("\n", " ") for t in translations]

    if len(translations) != len(summaries):
        print(f"[Warning] Mismatch in count: {len(translations)} translations for {len(summaries)} summaries.")
        print(f"[Warning] {len(translations) - 1} translations will be applied.")

    for i, summary in enumerate(summaries):
        summary["korean_summary"] = translations[i] if i < len(translations) else "[번역 누락]"
    
    last_idx = len(translations) - 1 if len(translations) < len(summaries) and len(translations) > 0 else len(translations)
    return summaries[:last_idx]


def write_document(section: str, summary: dict) -> None:
    print(f"Writing summary for `{summary['title']}` in {section} section")
    if not os.path.exists(DOCUMENT_PATH.format(section=section)):
        doc = Document()
        doc.add_heading(f"Papers Summary in {section} section", level=0)
        doc.save(DOCUMENT_PATH.format(section=section))
    doc = Document(DOCUMENT_PATH.format(section=section))
    doc.add_heading(summary["title"], level=2)
    p = doc.add_paragraph()
    p.add_run("URL: ").bold = True
    p.add_run(summary["url"])
    p.add_run("\n")
    p.add_run("Summary: ").bold = True
    p.add_run(summary["summary"])
    p.add_run("\n")
    p.add_run("Korean Summary: ").bold = True
    p.add_run(summary["korean_summary"])
    p.add_run("\n")
    doc.save(DOCUMENT_PATH.format(section=section))


def write_document_with_latest_papers(section: str, llm: ChatPerplexity):
    if os.path.exists("last_submitted_date.txt"):
        with open("last_submitted_date.txt", "r") as f:
            last_submitted_date = f.read().strip()
    else:
        last_submitted_date = None
    
    papers = get_papers(section, last_submitted_date)
    summaries = get_summary_from_abstract(papers)

    if summaries:
        summaries = add_translations(llm, summaries)
        for summary in summaries:
            write_document(section, summary)
    
    # Update the last submitted date
    if summaries:
        with open("last_submitted_date.txt", "w") as f:
            last_submitted_date = summaries[-1]["submitted_date"].strftime("%Y%m%d%H%M")
            f.write(last_submitted_date)

    
if __name__ == "__main__":
    # Initialize the LLM and agent
    llm = ChatPerplexity(model="sonar", pplx_api_key=PPLX_API_KEY, temperature=0.1)

    num_papers = input(f"How many papers do you want to fetch? (default: {BATCH_SIZE}): ")
    if not num_papers:
        num_papers = BATCH_SIZE
    else:
        num_papers = int(num_papers)
    for i in range(num_papers // BATCH_SIZE):
        write_document_with_latest_papers("cs.CV", llm)