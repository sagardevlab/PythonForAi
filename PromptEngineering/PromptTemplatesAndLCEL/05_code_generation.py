from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from lc_setup import llm

description = """
Retrieve the names and email addresses of all customers from the 'customers' table
who have made a purchase in the last 30 days. The table 'purchases' contains a
column 'purchase_date'.
"""

template = """Generate an SQL query based on this description: {description}

Return only the SQL query, no explanation.

SQL Query:
"""
prompt = PromptTemplate.from_template(template)

sql_chain = prompt | llm | StrOutputParser()

sql_query = sql_chain.invoke({"description": description})
print(sql_query)