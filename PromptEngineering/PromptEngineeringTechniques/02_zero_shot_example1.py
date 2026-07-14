from llm_helper import llm_model

params = {
    "max_tokens": 128,
    "temperature": 0.5
}

prompt = """Classify the following statement as true or false
'The Eiffel Tower is located in Berlin.'

Answer:
"""

response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response: {response}\n")