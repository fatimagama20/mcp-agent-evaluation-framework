from src.agent_workflow import AgentWorkflow


def test_customer_workflow():

    workflow = AgentWorkflow()

    result = workflow.process_request(
        "show customer details",
        customer_id=101
    )

    assert result["status"] == "success"

    assert result["customer_id"] == 101

    assert result["name"] == "John Smith"


def test_order_workflow():

    workflow = AgentWorkflow()

    result = workflow.process_request(
        "create order",
        customer_id=101
    )

    assert result["status"] == "success"

    assert result["order_id"] == 1001