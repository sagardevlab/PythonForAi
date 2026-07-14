import os 
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()

MODEL_ID = "claude-haiku-4-5"

def llm_model(prompt_txt, params=None):
    """Send a prompt to Claude and return the text response.

    params can override: max_tokens, temperature, top_p, top_k, system
    """

    default_params = {
        "max_tokens": 256,
        "temperature": 0.5,
    }
    if params:
        default_params.update(params)

    system = default_params.pop("system", None)

    kwargs = {
        "model": MODEL_ID,
        "messages": [{"role": "user", "content": prompt_txt}],
        **default_params,
    }
    if system:
        kwargs["system"] = system


    response = client.messages.create(**kwargs)
    return response.content[0].text

