from src.openai_agent import OpenAIAgent
from src.mcp_server import MCPServer


class AgentWorkflow:

    def __init__(self):

        self.agent = OpenAIAgent()
        self.server = MCPServer()

    def process_request(
        self,
        prompt,
        customer_id
    ):

        tool = self.agent.choose_tool(prompt)

        result = self.server.execute_tool(
            tool,
            customer_id=customer_id
        )

        return result