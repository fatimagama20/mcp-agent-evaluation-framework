from src.openai_client import OpenAILLM
from src.llm_evaluator import evaluate_answer


def test_france():

    llm = OpenAILLM()

    response = llm.ask(
        "What is the capital of France?"
    )

    assert evaluate_answer(
        "Paris",
        response
    )