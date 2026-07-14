from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lc_setup import llm

text = "The concert last night was an exhilarating experience with outstanding performances by all artists."
categories = "Entertainment, Food and Dining, Technology, Literature, Music"

template = """Classify the following text into exactly one of these categories: {categories}

Text: {text}

Respond with only the category name.

Category:
"""
prompt = PromptTemplate.from_template(template)

classification_chain = prompt | llm | StrOutputParser()

category = classification_chain.invoke({"text": text, "categories": categories})
print(category)