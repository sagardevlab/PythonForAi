from llm_helper import llm_model

params = {
    "max_tokens": 128,
    "temperature": 0.1,
}

prompt = "Complete this phrase: The future of AI is "

response = llm_model(prompt, params)
print(f"prompt: {prompt}\n")
print(f"response: {response}\n")