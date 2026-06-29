from src.tools import get_customer
from src.tools import create_order


class MCPServer:

    def __init__(self):

        self.tools = {

            "get_customer": {

                "description": "Retrieve customer details using customer ID.",

                "function": get_customer

            },

            "create_order": {

                "description": "Create a new customer order.",

                "function": create_order

            }

        }

    def list_tools(self):

        return list(self.tools.keys())


    def get_tool_descriptions(self):

        descriptions = []

        for name, tool in self.tools.items():

            descriptions.append(
                f"{name}: {tool['description']}"
            )

        return "\n".join(descriptions)


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

        tool = self.tools[tool_name]["function"]

        return tool(**kwargs)