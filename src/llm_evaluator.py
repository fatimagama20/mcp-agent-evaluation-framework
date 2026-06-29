from deepeval.metrics import AnswerRelevancyMetric

from deepeval.test_case import LLMTestCase


def evaluate_answer(expected, actual):

    # Existing pass/fail check
    passed = expected.lower() in actual.lower()

    # Create a DeepEval test case
    test_case = LLMTestCase(
        input=expected,
        actual_output=actual,
    )

    # Relevancy
    relevancy = AnswerRelevancyMetric(
        threshold=0.7
    )

    relevancy.measure(test_case)

    # # Faithfulness
    # faithfulness = FaithfulnessMetric(
    #     threshold=0.7
    # )

    # faithfulness.measure(test_case)

    return {
        "passed": passed,
        "relevancy": relevancy.score,
        # "faithfulness": faithfulness.score,
    }