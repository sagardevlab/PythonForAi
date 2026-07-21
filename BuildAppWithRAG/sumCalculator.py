import gradio as gr
from huggingface_hub import HfFolder

def add_numbers(Num1, Num2):
    return Num1+Num2

demo = gr.Interface(
    fn = add_numbers,
    inputs=[gr.Number(),gr.Number()],
    outputs=gr.Number()
)

demo.launch()