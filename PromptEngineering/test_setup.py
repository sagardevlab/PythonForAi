import os
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv() # reads .env into environment variables

client = Anthropic() # picks up Anthropic API Key automatically

message = client.messages.create(
    model="claude-haiku-4-5",
    max_tokens=100,
    messages=[{"role":"user", "content":"How are you."}],
)
print(message.content[0].text)