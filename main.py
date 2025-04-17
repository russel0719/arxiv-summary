from langchain_perplexity import ChatPerplexity
from langchain_core.messages import HumanMessage, SystemMessage

import os
import re
import arxiv
from typing import List
from datetime import datetime
from docx import Document

PPLX_API_KEY = os.getenv("PPLX_API_KEY")

client = arxiv.Client()
DOCUMENT_PATH = os.path.join(os.path.dirname(__file__), "{section}.docx")

    
def get_papers(section: str, last_submitted_date: str=None, max_results: int=50) -> List[arxiv.Result]:
    now = datetime.now().strftime("%Y%m%d%H%M")
    search = arxiv.Search(
        query=f"cat:{section} AND submittedDate:[{last_submitted_date} TO {now}]" if last_submitted_date else f"cat:{section}",
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
        "You will receive a numbered list of paper abstracts. "
        "Summarize and translate each one into Korean in 5 sentences."
        "Return the result in the format:\n\n"
        "1. <번역>\n2. <번역>\n...\n"
        "Do not skip any number. Only output the translations. Do not write in markdown format."
    )

    messages = [
        SystemMessage(content=prompt),
        HumanMessage(content="\n".join(formatted_abstracts))
    ]

    ai_message = llm.invoke(messages)
    print("Bulk Translations Received.")

    # 파싱: "1. 번역내용" 형식에서 번호를 기준으로 split
    translations = re.findall(r"\d+\.\s+(.*?)(?=\n\d+\.|\Z)", ai_message.content.strip(), re.DOTALL)
    translations = [t.strip().replace("\n", " ") for t in translations]

    if len(translations) != len(summaries):
        print(f"[Warning] Mismatch in count: {len(translations)} translations for {len(summaries)} summaries.")

    for i, summary in enumerate(summaries):
        summary["korean_summary"] = translations[i] if i < len(translations) else "[번역 누락]"

    return summaries[:len(translations)] if len(translations) < len(summaries) else summaries


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

    with open("last_submitted_date.txt", "w") as f:
        if summaries:
            last_submitted_date = summaries[-1]["submitted_date"].strftime("%Y%m%d%H%M")
        else:
            last_submitted_date = datetime.now().strftime("%Y%m%d%H%M")
        f.write(last_submitted_date)

    
if __name__ == "__main__":
    # Initialize the LLM and agent
    llm = ChatPerplexity(model="sonar", pplx_api_key=PPLX_API_KEY, temperature=0.1)

    write_document_with_latest_papers("cs.CV", llm)