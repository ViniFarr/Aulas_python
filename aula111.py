"""
import tkinter as tk 

lista = ["Vinicius" , "Erica" , "Tiago" , "Anthony" , "Erick"]
janela = tk.Tk()

janela.title('Tome a lista')
janela.config(background="#506155")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

janela.resizable(True, True)

titulo = tk.Label(text = ("Essa é a lista: "), fg='white',  bg='#506155',font = 120)
titulo.pack()

for i in range(5):
    nome = tk.Label(text = lista[i]) 
    nome.pack()


janela.mainloop()
"""
import tkinter as tk

numero_lista = []

def adicionar():
    numero = entrada.get()
    numero_lista.append(int(numero))
    entrada.delete(0)

def calculo():
    acomular = 0
    for i in range(len(numero_lista)):
        acomular = numero_lista[i] + acomular
    resultado = acomular / len(numero_lista)
    resultado_final.config(text=f"A media é: {resultado}")
    
    
janela = tk.Tk()

janela.title('Calculo')
janela.config(background="#506155")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

janela.resizable(True, True)

introducao = tk.Label(text = "Digite 5 numeros para o calculo da média: ", background="#506155",fg="white")
introducao.pack()

entrada = tk.Entry()
entrada.pack()

botao = tk.Button(text = "Adicionar" , command=adicionar )
botao.pack()

botao_result = tk.Button(text = "Resultado" , command=calculo )
botao_result.pack()

resultado_final = tk.Label(text = " " ,bg= "#506155", fg="white")
resultado_final.pack()
janela.mainloop()

"""
import tkinter as tk

janela = tk.Tk()

palavras = []

def adicionar():
    palavra = entrada.get()
    palavras.append(palavra)
    entrada.delete(0, tk.END)

def vereficar():
    maior_palavra = ' '
    for i in range(len(palavras)):
        if len(palavras[i]) > len(maior_palavra):
            maior_palavra = palavras[i]
            resultado.config(text =f"A maior palavra é: {maior_palavra}")
                  

janela.title('Palavras')

introducao = tk.Label(text= "Digite 5 palavras e descubra quem é maior: ")
introducao.pack()
entrada = tk.Entry()
entrada.pack()
clicar = tk.Button(text= "Adicione", command= adicionar)
clicar.pack()
clicar2 = tk.Button(text= "Resultado", command= vereficar)
clicar2.pack()
resultado = tk.Label(text= " ")
resultado.pack()

janela.mainloop()

#Atividade 4:


import tkinter as tk

janela = tk.Tk()

numeros = []
lista = []

def adicionar():
    numero = entrada.get()
    numero = int(numero)
    if numero % 2 == 0:
        numeros.append(numero)
    entrada.delete(0, tk.END)

def vereficar():
    resultado.config(text =f"Os numeros pares são: {numeros}")
            
                  

janela.title('Palavras')

introducao = tk.Label(text= "Digite 10 numeros e descubra quem é par: ")
introducao.pack()
entrada = tk.Entry()
entrada.pack()
clicar = tk.Button(text= "Adicione", command= adicionar)
clicar.pack()
clicar2 = tk.Button(text= "Resultado", command= vereficar)
clicar2.pack()
resultado = tk.Label(text= " ")
resultado.pack()

janela.mainloop()

Atividade 5:

import tkinter as tk

janela = tk.Tk()

palavras = []


def adicionar():
    palavra = entrada.get()
    palavras.append(palavra)
    entrada.delete(0, tk.END)

def remover():
    palavra_remover = entrada2.get()
    for i in palavras:
        if palavra_remover == i:
            palavras.remove(i)

    resultado.config(text =f"Essa é a lista agora: {palavras}")
            
                  

janela.title('Palavras')

introducao = tk.Label(text= "Digite 5 produtos: ")
introducao.pack()
entrada = tk.Entry()
entrada.pack()
clicar = tk.Button(text= "Adicione", command= adicionar)
clicar.pack()
introducao2 = tk.Label(text= "Digite 1 produtos para remover: ")
introducao2.pack()
entrada2 = tk.Entry()
entrada2.pack()
clicar2 = tk.Button(text= "Resultado", command= remover)
clicar2.pack()
resultado = tk.Label(text= " ")
resultado.pack()

janela.mainloop()

Atividade 6:

import tkinter as tk

janela = tk.Tk()

palavras = []


def adicionar():
    numero = entrada.get()
    palavras.append(palavra)
    entrada.delete(0, tk.END)

def remover():
    for i in palavras:
        if palavra_remover == i:
            palavras.remove(i)

    resultado.config(text =f"Essa é a lista agora: {palavras}")
            
                  

janela.title('Palavras')

introducao = tk.Label(text= "Digite 5 idades: ")
introducao.pack()
entrada = tk.Entry()
entrada.pack()
clicar = tk.Button(text= "Adicione", command= adicionar)
clicar.pack()
clicar2 = tk.Button(text= "Resultado", command= calculo)
clicar2.pack()
resultado = tk.Label(text= " ")
resultado.pack()

janela.mainloop()

"""
