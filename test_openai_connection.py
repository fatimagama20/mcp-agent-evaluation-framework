from src.openai_client import OpenAILLM

llm = OpenAILLM()

answer = llm.ask(
    "What is the capital of France?"
)

print(answer)