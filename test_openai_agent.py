from src.openai_agent import OpenAIAgent

agent = OpenAIAgent()

result = agent.choose_tool(
    "Show customer 101"
)

print(result)

# prompts = [
#     "Show customer details",
#     "Create an order",
#     "Delete everything"
# ]

# for prompt in prompts:

#     print("=" * 50)
#     print(f"User Prompt : {prompt}")

#     tool = agent.choose_tool(prompt)

#     print(f"Selected Tool : {tool}")