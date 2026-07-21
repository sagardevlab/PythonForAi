from anthropic import Anthropic
import os

client = Anthropic(
    api_key="Anthropic_Key"
)

models = client.models.list()

for model in models:
    print(model.id)