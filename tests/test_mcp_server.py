from src.mcp_server import MCPServer


def test_list_tools():

    server = MCPServer()

    tools = server.list_tools()

    assert "get_customer" in tools

    assert "create_order" in tools


def test_execute_customer():

    server = MCPServer()

    result = server.execute_tool(
        "get_customer",
        customer_id=101
    )

    assert result["status"] == "success"

    assert result["customer_id"] == 101

    assert result["name"] == "John Smith"

def test_invalid_tool():

    server = MCPServer()

    result = server.execute_tool(
        "delete_everything"
    )

    assert result["status"] == "error"
    assert result["message"] == "Unknown tool: delete_everything"