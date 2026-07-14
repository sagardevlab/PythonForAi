from langchain_core.prompts import PromptTemplate
from llm_setup import llm

prompt = PromptTemplate.from_template("Tell me one {adjective} joke about {topic}")
input_ = {"adjective":"funny", "topic":"cats"}

print(prompt.invoke(input_))
