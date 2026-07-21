import gradio as gr
from anthropic import Anthropic
import os

client = Anthropic(
    api_key="Anthropic_Key"
)

def generate_response(prompt):
    response = client.messages.create(
        model="claude-sonnet-5",
        max_tokens=1024,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    for block in response.content:
        if block.type == "text":
            return block.text

    return "No text response generated"

demo = gr.Interface(
    fn=generate_response,
    inputs=gr.Textbox(
        label="Enter your prompt",
        placeholder="Ask Claude anything...",
        lines=5
    ),
    outputs=gr.Textbox(
        label="Claude Response",
        lines=10
    ),
    title="Anthropic Claude Chat App",
    description="Enter a prompt and get a response from Claude."
)

demo.launch()

