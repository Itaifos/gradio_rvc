import gradio as gr
from app import multiply_by_two 

interface = gr.Interface(
    fn=multiply_by_two,  # Função que será chamada
    inputs="number",     # Tipo de input (número)
    outputs="text"       # Tipo de output (texto)
    # title="Multiplicador de Números",
    # description="Insira um número e ele será multiplicado por 2."
)

if __name__ == "__main__":
    interface.launch()
