import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic

load_dotenv()

llm = ChatAnthropic(
    model="claude-haiku-4-5",
    max_tokens=256,
    temperature=0.5,
)