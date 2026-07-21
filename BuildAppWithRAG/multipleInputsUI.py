import gradio as gr

def process_number_and_text(number, text):
    return f"The number is {number} and the text is '{text}'."

demo = gr.Interface(
    fn = process_number_and_text,
    inputs = [
        gr.Number(label = "Enter a number"),
        gr.Textbox(label="Enter a text")
    ],
    outputs = gr.Textbox(label = "Output")
)

demo.launch()