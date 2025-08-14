PROMPT = """You are an expert in Computer Vision. Given the title and abstract of a research paper, evaluate each paper’s *scientific quality and impact* within the field of computer vision.

Paper is provided in the format:
- Title: <paper title>
- Abstract: <paper abstract>

In addition, use the following statistical summary of previously evaluated papers to guide your scoring. For each of the 9 criteria, you are provided with the mean (average) and standard deviation (std). When scoring, consider whether the current paper’s quality on that criterion appears above, near, or below the previous mean, and adjust your score accordingly, while still staying within the original scale.

Statistical summary (mean ± std) from previously evaluated papers:
- problem_significance: μ={ps_mu:.2f}, σ={ps_sigma:.2f}
- novelty: μ={n_mu:.2f}, σ={n_sigma:.2f}
- technical_depth: μ={td_mu:.2f}, σ={td_sigma:.2f}
- practical_impact: μ={pi_mu:.2f}, σ={pi_sigma:.2f}
- result_quality: μ={rq_mu:.2f}, σ={rq_sigma:.2f}
- comparative_evaluation: μ={ce_mu:.2f}, σ={ce_sigma:.2f}
- broader_impact: μ={bi_mu:.2f}, σ={bi_sigma:.2f}
- field_contribution: μ={fc_mu:.2f}, σ={fc_sigma:.2f}
- clarity: μ={c_mu:.2f}, σ={c_sigma:.2f}

When scoring a paper, still use the original scale per criterion (e.g. 0-15, 0-10, 0-5), but adjust the score considering how this paper compares to these prior averages and deviations. This helps maintain consistency and relative calibration across many evaluations.

Scoring Guidelines (used per paper):
1. problem_significance (0-15): Does the paper address a meaningful and important problem in computer vision?
2. novelty (0-15): Are the ideas, techniques, or approaches new compared to prior work?
3. technical_depth (0-15): Does the method demonstrate strong theoretical, algorithmic, or methodological rigor?
4. practical_impact (0-10): Is the method applicable or adaptable to real-world scenarios or other tasks?
5. result_quality (0-10): Are the reported results strong, convincing, and indicative of improvement?
6. comparative_evaluation (0-10): Does the abstract indicate thorough comparison with baselines or SOTA?
7. broader_impact (0-10): Could this work have influence on industry, society, or interdisciplinary areas?
8. field_contribution (0-10): Does the paper propose new directions, datasets, or reusable techniques for CV research?
9. clarity (0-5): Is the abstract clearly written and easy to understand, including key contributions and methods?

Return your answer as JSON format with the key each criterion and the value as the corresponding score."""


from langchain_perplexity import ChatPerplexity
from langchain_core.messages import HumanMessage, SystemMessage

import os
from dotenv import load_dotenv
import arxiv
import csv
import numpy as np
from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import datetime

load_dotenv()
PPLX_API_KEY = os.getenv("PPLX_API_KEY")
EXCEPT_KEYWORDS = ["robot", "security", "cripto", "emotion", "study", "report", "survey", "review"]
BATCH_SIZE = 1

client = arxiv.Client(page_size=100, delay_seconds=3, num_retries=5)


class EvaluationResult(BaseModel):
    problem_significance: int #= Field(description="Score for problem significance (0-15)")
    novelty: int #= Field(description="Score for novelty (0-15)")
    technical_depth: int #= Field(description="Score for technical depth (0-15)")
    practical_impact: int #= Field(description="Score for practical impact (0-10)")
    result_quality: int #= Field(description="Score for result quality (0-10)")
    comparative_evaluation: int #= Field(description="Score for comparative evaluation (0-10)")
    broader_impact: int #= Field(description="Score for broader impact (0-10)")
    field_contribution: int #= Field(description="Score for field contribution (0-10)")
    clarity: int #= Field(description="Score for clarity (0-5)")

    @property
    def total_score(self) -> int:
        return (self.problem_significance + self.novelty + self.technical_depth +
                self.practical_impact + self.result_quality + self.comparative_evaluation +
                self.broader_impact + self.field_contribution + self.clarity)


def get_evaluation_metrics(filename: str = "evaluations.csv") -> Dict[str, tuple[float, float]]:
    if not os.path.exists(filename):
        return {}

    metrics = {
        "problem_significance": [],
        "novelty": [],
        "technical_depth": [],
        "practical_impact": [],
        "result_quality": [],
        "comparative_evaluation": [],
        "broader_impact": [],
        "field_contribution": [],
        "clarity": [],
        "total_score": []
    }
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            if len(row) < 13:
                continue
            for i, key in enumerate(metrics.keys()):
                metrics[key].append(int(row[i + 3]))  # Adjust index to match scores
    for key in metrics:
        if metrics[key]:
            metrics[key] = [np.mean(metrics[key]), np.std(metrics[key])]
        else:
            metrics[key] = [0, 0]
    return metrics


def get_papers(last_submitted_date: str=None, max_results: int=BATCH_SIZE) -> List[arxiv.Result]:
    if last_submitted_date:
        dt = datetime.fromisoformat(last_submitted_date)
        last_submitted_date = int(dt.strftime("%Y%m%d%H%M")) + 1
    now = datetime.now().strftime("%Y%m%d%H%M")
    except_query = " OR ".join([f"ti:{keyword}" for keyword in EXCEPT_KEYWORDS])
    default_query = f"cat:cs.CV AND submittedDate:[{last_submitted_date} TO {now}]" if last_submitted_date else f"cat:cs.CV"
    search = arxiv.Search(
        query=f"{default_query} ANDNOT ({except_query})",
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate,
        sort_order=arxiv.SortOrder.Ascending,
    )
    results = list(client.results(search))
    return results


def papers_to_message(papers: List[arxiv.Result]) -> HumanMessage:
    messages = []
    for paper in papers:
        title = paper.title.strip()
        abstract = paper.summary.strip().replace('\n', ' ')
        messages.append(f"- Title: {title}\n- Abstract: {abstract}")
    return HumanMessage(content="\n\n---\n".join(messages))


def evaluate_papers(llm: ChatPerplexity, paper: arxiv.Result, metrics: Dict[str, tuple[float, float]]) -> EvaluationResult:
    if not paper:
        return None

    ps_mu, ps_sigma = metrics.get("problem_significance")
    n_mu, n_sigma = metrics.get("novelty")
    td_mu, td_sigma = metrics.get("technical_depth")
    pi_mu, pi_sigma = metrics.get("practical_impact")
    rq_mu, rq_sigma = metrics.get("result_quality")
    ce_mu, ce_sigma = metrics.get("comparative_evaluation")
    bi_mu, bi_sigma = metrics.get("broader_impact")
    fc_mu, fc_sigma = metrics.get("field_contribution")
    c_mu, c_sigma = metrics.get("clarity")
    prompt = PROMPT.format(
        ps_mu=ps_mu, ps_sigma=ps_sigma,
        n_mu=n_mu, n_sigma=n_sigma,
        td_mu=td_mu, td_sigma=td_sigma,
        pi_mu=pi_mu, pi_sigma=pi_sigma,
        rq_mu=rq_mu, rq_sigma=rq_sigma,
        ce_mu=ce_mu, ce_sigma=ce_sigma,
        bi_mu=bi_mu, bi_sigma=bi_sigma,
        fc_mu=fc_mu, fc_sigma=fc_sigma,
        c_mu=c_mu, c_sigma=c_sigma
    )
    messages = [SystemMessage(content=prompt), papers_to_message([paper])]
    response = llm.invoke(messages) # type: EvaluationResult
    return response


def write_evaluation_to_file(paper: arxiv.Result, evaluation: EvaluationResult, filename: str = "evaluations.csv"):
    title = paper.title.strip()
    url = paper.entry_id
    published = paper.published
    if not os.path.exists(filename):
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(["Title", "Arxiv Link", "Submission", "Problem Significance", "Novelty", "Technical Depth",
                            "Practical Impact", "Result Quality", "Comparative Evaluation",
                            "Broader Impact", "Field Contribution", "Clarity", "Total Score"])
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([
            title,
            url,
            published,
            evaluation.problem_significance,
            evaluation.novelty,
            evaluation.technical_depth,
            evaluation.practical_impact,
            evaluation.result_quality,
            evaluation.comparative_evaluation,
            evaluation.broader_impact,
            evaluation.field_contribution,
            evaluation.clarity,
            evaluation.total_score
        ])
    print(f"Title: {title} evaluated with total score: {evaluation.total_score}")


def main(metrics: Dict[str, tuple[float, float]]):
    llm = ChatPerplexity(model="sonar", api_key=PPLX_API_KEY, temperature=0.0)
    llm = llm.with_structured_output(EvaluationResult)
    
    last_submitted_date = "202501010000"  # You can set this to a specific date if needed
    if os.path.exists("evaluations.csv"):
        with open("evaluations.csv", "r", encoding="utf-8") as file:
            reader = csv.reader(file)
            last_row = list(reader)[-1]
            last_submitted_date = last_row[2].strip() if len(last_row) > 2 else None

    papers = get_papers(last_submitted_date=last_submitted_date)
    if not papers:
        return
    evaluation = evaluate_papers(llm, papers[0], metrics)
    write_evaluation_to_file(papers[0], evaluation)


if __name__ == "__main__":
    metrics = get_evaluation_metrics()
    print("Evaluation metrics:")
    for key, (mean, std) in metrics.items():
        print(f"{key}: {mean:.2f} ± {std:.2f}")
    
    num_iters = input(f"How many times do you want to evaluate? (default: exit): ")
    if not num_iters:
        print("Exiting without evaluation.")
    else:
        num_iters = int(num_iters)
        for  _ in range(num_iters):
            try:
                main(metrics)
            except Exception as e:
                print(f"Error occurred: {e}. Retrying...")
                continue