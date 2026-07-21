import gradio as gr

def process_txt(text):
    return f"You entered: '{text}'"

demo = gr.Interface(
    fn = process_txt,
    inputs = gr.Textbox(label="Enter Some Text"),
    outputs = gr.Textbox(label="Output")
)

demo.launch()