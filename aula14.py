"""
Atividade 1:
"""
import tkinter as tk

lista = []

def verificar():
    verificador = entrada.get()
    verificador = int(verificador)
    if verificador == 1:
        pergunta = tk.Label(text="Digite oque sera empilhado: ").pack()
        entrada2 = tk.Entry()
        entrada2.pack()

        def adicionar():
            vai_pilha = entrada2.get()
            lista.append(vai_pilha)
            entrada2.delete(0, tk.END)

        botao2 = tk.Button(text="Adicionar", command=adicionar)
        botao2.pack()

    elif verificador == 2:

        final = tk.Label(text=f"A pilha é de: {lista}" ).pack()
janela = tk.Tk()
janela.title('Pilha')
janela.config(background="white")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

introducao = tk.Label(text="Escolha 1 das seguintes alternativas: ", background="white").pack()
alternativa1 = tk.Label(text="1-Adicionar a pilha", background="white").pack()
alternativa2 = tk.Label(text="2-Ver pilha              ", background="white").pack()

entrada = tk.Entry()
entrada.pack()
botao = tk.Button(text="Confirmar", command=verificar)
botao.pack()



janela.mainloop()
"""
Atividade 2:

import tkinter as tk

pilha = []

def verificar():
    guardar = entrada.get()
    if guardar == "sair" or guardar == "Sair":
        final.config(text=f" A pilha é composta de: {pilha}")
    pilha.append(guardar)
    entrada.delete(0, tk.END)
    

janela = tk.Tk()
janela.title("Atividade 2")
janela.config(background="white")
janela.geometry("1200x900")
janela.maxsize(width=1800, height=1500)
janela.minsize(width=300, height=300)

introducao = tk.Label(text= "Informe oque sera colocado em pilha: ")
introducao.pack()
entrada = tk.Entry()
entrada.pack()
botao = tk.Button(text= "CONFIRMAR", command=verificar )
botao.pack()
final = tk.Label(text= " ", background="white")
final.pack()

janela.mainloop()

Atividade 3:

import tkinter as tk

pilha = []
lista = []
def desempilhar():
    
    if len(pilha) == len(lista):
        final2 = tk.Label(text= "Não foi possivel pois a lista esta vazia", background="white")
        final2.pack()  
        final.config(text=f" ")
        return
    else:        
        remover = pilha.pop()
        final.config(text=f" A pilha é composta de: {pilha}")

def verificar():
    
    guardar = entrada.get()
    if guardar == "sair" or guardar == "Sair":
        final.config(text=f" A pilha é composta de: {pilha}")
    pilha.append(guardar)
    entrada.delete(0, tk.END)


    

janela = tk.Tk()
janela.title("Atividade 2")
janela.config(background="white")
janela.geometry("1200x900")
janela.maxsize(width=1800, height=1500)
janela.minsize(width=300, height=300)

introducao = tk.Label(text= "Informe oque sera colocado em pilha: ")
introducao.pack()
entrada = tk.Entry()
entrada.pack()
botao = tk.Button(text= "CONFIRMAR", command=verificar )
botao.pack()
botao2 = tk.Button(text= "DESIMPILHAR", command=desempilhar)
botao2.pack()
final = tk.Label(text= " ", background="white")
final.pack()

janela.mainloop()

"""






