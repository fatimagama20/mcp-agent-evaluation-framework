from src.agent import Agent
from src.mcp_server import MCPServer


class AgentWorkflow:

    def __init__(self):

        self.agent = Agent()
        self.server = MCPServer()

    def process_request(
        self,
        prompt,
        customer_id
    ):

        # Step 1 - Agent decides which tool to use
        tool = self.agent.decide_tool(prompt)

        print(f"Agent selected tool: {tool}")

        # Step 2 - MCP Server executes the tool
        result = self.server.execute_tool(
            tool,
            customer_id=customer_id
        )

        return result