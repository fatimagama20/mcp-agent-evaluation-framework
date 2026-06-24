from src.tools import get_customer
from src.tools import create_order


class Agent:

    def decide_tool(self, prompt):

        if "customer" in prompt.lower():
            return "get_customer"

        if "order" in prompt.lower():
            return "create_order"

        return "unknown"