from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lc_setup import llm

content = """
The rapid advancement of technology in the 21st century has transformed various
industries, including healthcare, education, and transportation. Innovations such
as artificial intelligence, machine learning, and the Internet of Things have
revolutionized how we approach everyday tasks and complex problems. AI-powered
diagnostic tools are improving the accuracy and speed of medical diagnoses, while
smart transportation systems are making cities more efficient. Moreover, online
learning platforms are making education more accessible to people around the world.
"""

template = "Summarize the following content in one sentence:\n\n{content}"
prompt = PromptTemplate.from_template(template)

summarize_chain = prompt | llm | StrOutputParser()

summary = summarize_chain.invoke({"content": content})
print(summary)