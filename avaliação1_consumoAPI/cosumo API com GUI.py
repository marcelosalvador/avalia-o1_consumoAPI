import requests
import tkinter as tk
from tkinter import messagebox

def solicitar_frase():
    return entry_frase.get()

def traduzir_para_yoda(frase):
    URL = f"https://api.funtranslations.com/translate/yoda.json?text={frase}"
    resposta = requests.get(URL)
    dados = resposta.json()
    return dados['contents']['translated']

def traduzir_para_pirata(frase):
    URL = f"https://api.funtranslations.com/translate/pirate.json?text={frase}"
    resposta = requests.get(URL)
    dados = resposta.json()
    return dados['contents']['translated']

def traduzir_para_minion(frase):
    URL = f"https://api.funtranslations.com/translate/minion.json?text={frase}"
    resposta = requests.get(URL)
    dados = resposta.json()
    return dados['contents']['translated']

def traduzir_e_exibir():
    frase_usuario = solicitar_frase()
    if not frase_usuario:
        messagebox.showerror("Erro", "Por favor, insira uma frase.")
        return

    dados_yoda = traduzir_para_yoda(frase_usuario)
    dados_pirata = traduzir_para_pirata(frase_usuario)
    dados_minion = traduzir_para_minion(frase_usuario)

    texto_yoda.delete(1.0, tk.END)
    texto_yoda.insert(tk.END, f"Yoda: \n{dados_yoda}")

    texto_pirata.delete(1.0, tk.END)
    texto_pirata.insert(tk.END, f"Pirata: \n{dados_pirata}")

    texto_minion.delete(1.0, tk.END)
    texto_minion.insert(tk.END, f"Minion: \n{dados_minion}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Tradutor de Idiomas Fictícios")

# Criação dos widgets
label_frase = tk.Label(janela, text="Digite uma frase em inglês:")
label_frase.pack()

entry_frase = tk.Entry(janela, width=50)
entry_frase.pack()

botao_traduzir = tk.Button(janela, text="Traduzir", command=traduzir_e_exibir)
botao_traduzir.pack()

texto_yoda = tk.Text(janela, height=5, width=50)
texto_yoda.pack()

texto_pirata = tk.Text(janela, height=5, width=50)
texto_pirata.pack()

texto_minion = tk.Text(janela, height=5, width=50)
texto_minion.pack()

# Inicialização do loop principal
janela.mainloop()
