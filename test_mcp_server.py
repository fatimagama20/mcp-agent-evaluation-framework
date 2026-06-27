from src.mcp_server import MCPServer

server = MCPServer()

print("Available Tools")
print(server.list_tools())

print()

result = server.execute_tool(
    "get_customer",
    customer_id=101
)

print(result)