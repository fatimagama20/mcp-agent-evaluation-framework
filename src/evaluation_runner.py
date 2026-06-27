import json

from src.openai_client import OpenAILLM
from src.llm_evaluator import evaluate_answer

llm = OpenAILLM()

results = []

with open(
    "datasets/llm_test_cases.json"
) as f:

    data = json.load(f)

for test_case in data:

    answer = llm.ask(
        test_case["question"]
    )

    passed = evaluate_answer(
        test_case["expected_answer"],
        answer
    )

    results.append(
        {
            "question": test_case["question"],
            "answer": answer,
            "passed": passed
        }
    )

accuracy = (
    sum(
        result["passed"]
        for result in results
    )
    / len(results)
) * 100

hallucination_rate = 100 - accuracy

print(f"Accuracy: {accuracy}%")

print(
    f"Hallucination Rate: "
    f"{hallucination_rate}%"
)

print(results)

report = {
    "accuracy": accuracy,
    "hallucination_rate": hallucination_rate,
    "results": results
}

with open(
    "reports/evaluation_report.json",
    "w"
) as f:

    json.dump(
        report,
        f,
        indent=4
    )