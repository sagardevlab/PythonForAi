from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lc_setup import llm

#1 Template with two variabels
template = "Tell me a {adjective} joke about {content}."
prompt = PromptTemplate.from_template(template)

# See how formatting works
print(prompt.format(adjective="funny", content="chickens"))
# -> "Tell me a funny joke about chickens."

#2 Build an LCEL chain: template | llm | parser
joke_chain = prompt | llm | StrOutputParser()

# 3. Invoke with different variables — same chain, reusable
print(joke_chain.invoke({"adjective": "funny", "content": "chickens"}))
print(joke_chain.invoke({"adjective": "sad", "content": "fish"}))