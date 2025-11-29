import gradio as gr

def query_kb(message, history):
    response = f"Knowledge Base Agent Answer: {message}"  # Replace later with real agent
    history.append((message, response))
    return history, ""

demo = gr.ChatInterface(fn=query_kb, title="Knowledge Base Agent Demo")
if __name__ == "__main__":
    demo.launch(share=True)  # Creates public link instantly
