import gradio as gr

def count_files(files):
    return f"Number of files Uploaded: {len(files)}"

demo = gr.Interface(
    fn = count_files,
    inputs = gr.File(file_count = "multiple",
                    type = "filepath",
                    label = "Upload or Drag Files Here"),
    outputs = gr.Textbox(label = "Number of files Uploaded"),
)

demo.launch()