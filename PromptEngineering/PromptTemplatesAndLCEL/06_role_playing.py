from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lc_setup import llm

role = "Dungeons & Dragons game master"
tone = "engaging and immersive"

template = """You are an expert {role}. I have this question: {question}
I would like our conversation to be {tone}.

Answer:
"""
prompt = PromptTemplate.from_template(template)

roleplay_chain = prompt | llm | StrOutputParser()

print("D&D Game Master bot ready. Type 'quit' to exit.\n")
while True:
    query = input("Question: ")
    if query.lower() in ["quit", "exit", "bye"]:
        print("Answer: Goodbye!")
        break
    response = roleplay_chain.invoke({"role": role, "question": query, "tone": tone})
    print("Answer:", response, "\n")