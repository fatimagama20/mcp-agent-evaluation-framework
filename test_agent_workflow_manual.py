from src.agent_workflow import AgentWorkflow

workflow = AgentWorkflow()

response = workflow.process_request(
    "show customer details",
    customer_id=101
)

print(response)