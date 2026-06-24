from src.evaluator import hallucination_check


def test_hallucination():

    expected = "Paris"

    generated = "Berlin"

    result = hallucination_check(
        expected,
        generated
    )

    assert result is False