from src.tools import get_customer
from src.tools import create_order


class MCPServer:

    def __init__(self):

        self.tools = {
            "get_customer": get_customer,
            "create_order": create_order
        }

    def list_tools(self):

        return list(self.tools.keys())

    def execute_tool(
        self,
        tool_name,
        **kwargs
    ):

        if tool_name not in self.tools:

            return {
                "status": "error",
                "message": f"Unknown tool: {tool_name}"
            }

        tool = self.tools[tool_name]

        return tool(**kwargs)