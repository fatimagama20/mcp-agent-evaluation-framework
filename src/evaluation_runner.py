import json
import time

from src.openai_client import OpenAILLM
from src.llm_evaluator import evaluate_answer
from src.html_report import HTMLReport

llm = OpenAILLM()

results = []

with open(
    "datasets/llm_test_cases.json"
) as f:

    data = json.load(f)

for test_case in data:
    start = time.perf_counter()

    answer = llm.ask(
        test_case["question"]
    )

    end = time.perf_counter()
    latency = end - start

    evaluation = evaluate_answer(
        test_case["expected_answer"],
        answer
    )

    results.append(
        {
            "question": test_case["question"],
            "expected_answer": test_case["expected_answer"],
            "answer": answer,
            "passed": evaluation["passed"],
            "relevancy": evaluation["relevancy"],
            "latency": round(latency, 2),
            # "faithfulness": evaluation["faithfulness"]
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

average_relevancy = sum(
    result["relevancy"]
    for result in results
) / len(results)

average_latency = sum(
    result["latency"]
    for result in results
) / len(results)

# average_faithfulness = sum(
#     result["faithfulness"]
#     for result in results
# ) / len(results)

print(f"Accuracy: {accuracy}%")

print(
    f"Hallucination Rate: "
    f"{hallucination_rate}%"
)

print(f"Average Relevancy: {average_relevancy:.2f}")

print(
    f"Average Latency: "
    f"{average_latency:.2f} sec"
)

# print(f"Average Faithfulness: {average_faithfulness:.2f}")

# print(results)

print("\nEvaluation Results")
print("-" * 60)

for result in results:

    print(f"Question   : {result['question']}")

    print(f"Expected   : {result['expected_answer']}")

    print(f"Answer     : {result['answer']}")

    print(f"Passed     : {result['passed']}")

    print(f"Relevancy  : {result['relevancy']:.2f}")

    print("-" * 60)

report = {

    "accuracy": accuracy,

    "hallucination_rate": hallucination_rate,

    "average_relevancy": average_relevancy,

    "average_latency": average_latency,

    # "average_faithfulness": average_faithfulness,

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
    html = HTMLReport()

html.generate(report)

print("\nHTML report generated successfully!")

print("reports/evaluation_report.html")