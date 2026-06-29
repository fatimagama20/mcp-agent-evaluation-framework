from deepeval.metrics import AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

from src.openai_client import OpenAILLM


def test_answer_relevancy():

    llm = OpenAILLM()

    response = llm.ask(
        "What is the capital of France?"
    )

    print("\nModel Response:")
    print(response)

    test_case = LLMTestCase(

        input="What is the capital of France?",

        actual_output=response

    )

    metric = AnswerRelevancyMetric(
        threshold=0.7
    )

    metric.measure(test_case)

    print("\nRelevancy Score:")
    print(metric.score)

    assert metric.score >= 0.7