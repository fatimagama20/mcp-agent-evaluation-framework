from src.openai_client import OpenAILLM
from src.mcp_server import MCPServer


class OpenAIAgent:

    def __init__(self):

        self.llm = OpenAILLM()
        self.server = MCPServer()

    def choose_tool(self, prompt):

        available_tools = self.server.get_tool_descriptions()

        system_prompt = f"""
You are an AI agent responsible for selecting the correct tool.

Available tools:

{available_tools}

Rules:
- Return ONLY the tool name.
- Do not explain.
- If nothing matches, return unknown.

User Request:
{prompt}
"""

        return self.llm.ask(system_prompt).strip()