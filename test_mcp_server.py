from src.mcp_server import MCPServer

server = MCPServer()

print("Available Tools")
print(server.list_tools())

print()

result = server.execute_tool(
    "get_customer",
    customer_id=101
)

print("\nEvaluation Results")
print("-" * 60)

for result in results:

    print(f"Question   : {result['question']}")

    print(f"Expected   : {result['expected_answer']}")

    print(f"Answer     : {result['answer']}")

    print(f"Passed     : {result['passed']}")

    print(f"Relevancy  : {result['relevancy']:.2f}")

    print("-" * 60)