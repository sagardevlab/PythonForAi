from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lc_setup import llm

content = """
The solar system consists of the Sun, eight planets, their moons, dwarf planets,
and smaller objects like asteroids and comets. The inner planets—Mercury, Venus,
Earth, and Mars—are rocky and solid. The outer planets—Jupiter, Saturn, Uranus,
and Neptune—are much larger and gaseous.
"""

template = """Answer the question based only on the content below.
Respond "Unsure about answer" if not sure about the answer.

Content: {content}

Question: {question}

Answer:
"""
prompt = PromptTemplate.from_template(template)

qa_chain = prompt | llm | StrOutputParser()

answer = qa_chain.invoke({
    "question": "Which planets in the solar system are rocky and solid?",
    "content": content,
})
print(answer)

# Try a question the content can't answer — you should get "Unsure about answer"
print(qa_chain.invoke({
    "question": "How many moons does Jupiter have?",
    "content": content,
}))