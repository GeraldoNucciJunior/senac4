"""
Rotina simples com interface gráfica (Tkinter) onde o usuário
digita um valor numérico e o sistema exibe o resultado de um cálculo.

Como executar:
    python tela_valor.py

Não precisa instalar nada: o Tkinter já vem com o Python padrão.
"""

import tkinter as tk
from tkinter import messagebox


def calcular():
    """Lê o valor digitado, valida e exibe o resultado."""
    texto = entrada_valor.get()

    try:
        valor = float(texto.replace(",", "."))  # aceita vírgula ou ponto
    except ValueError:
        messagebox.showerror("Erro", "Digite um número válido.")
        return

    dobro = valor * 2
    quadrado = valor ** 2

    resultado_texto = (
        f"Valor digitado: {valor:.2f}\n"
        f"Dobro: {dobro:.2f}\n"
        f"Quadrado: {quadrado:.2f}"
    )
    label_resultado.config(text=resultado_texto)


def limpar():
    """Limpa o campo de entrada e o resultado."""
    entrada_valor.delete(0, tk.END)
    label_resultado.config(text="")
    entrada_valor.focus()


# ---------- Montagem da janela ----------
janela = tk.Tk()
janela.title("Digite um valor")
janela.geometry("320x260")
janela.resizable(False, False)

label_instrucao = tk.Label(janela, text="Digite um valor numérico:", font=("Arial", 11))
label_instrucao.pack(pady=(20, 5))

entrada_valor = tk.Entry(janela, font=("Arial", 12), justify="center")
entrada_valor.pack(pady=5, ipady=4, padx=20, fill="x")
entrada_valor.focus()
entrada_valor.bind("<Return>", lambda evento: calcular())  # Enter também calcula

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=15)

botao_calcular = tk.Button(frame_botoes, text="Calcular", command=calcular, width=10)
botao_calcular.grid(row=0, column=0, padx=5)

botao_limpar = tk.Button(frame_botoes, text="Limpar", command=limpar, width=10)
botao_limpar.grid(row=0, column=1, padx=5)

label_resultado = tk.Label(janela, text="", font=("Arial", 11), justify="left")
label_resultado.pack(pady=10)

janela.mainloop()
