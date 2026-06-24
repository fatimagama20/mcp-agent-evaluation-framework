from src.agent import Agent


def test_customer_tool():

    agent = Agent()

    tool = agent.decide_tool(
        "show customer details"
    )

    assert tool == "get_customer"


def test_order_tool():

    agent = Agent()

    tool = agent.decide_tool(
        "create order"
    )

    assert tool == "create_order"