from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field   # modern import (the lab used langchain_core.pydantic_v1)
from llm_setup import llm

# Define the desired data structure
class Joke(BaseModel):
    setup: str = Field(description="question to set up a joke")
    punchline: str = Field(description="answer to resolve the joke")

output_parser = JsonOutputParser(pydantic_object=Joke)
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": format_instructions},
)

chain = prompt | llm | output_parser
result = chain.invoke({"query": "Tell me a joke."})
print(result)              # a real Python dict
print(result["setup"])
print(result["punchline"])