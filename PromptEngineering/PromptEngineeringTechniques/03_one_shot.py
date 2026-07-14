from llm_helper import llm_model

params = {
    "max_tokens": 256,
    "temperature": 0.3
}

prompt = """Here is an example of translating a sentence from English to French:
English: "How is the weather today?"
French: "Comment est le temps aujourd'hui?"

Now, translate the following sentence from English to French:
English: "Where is the nearest supermarket?"
French:
"""

response = llm_model(prompt, params)
print(f"response: {response}\n")