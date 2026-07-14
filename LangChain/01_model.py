from llm_setup import llm

response = llm.invoke("Complete this sentence: In today's sales meeting, we ")
print(response.content)

print(llm.invoke("Who is man's best friend?").content)
