"""
import tkinter as tk

def troca_valor():
    atualizado = novo_texto.get()
    titulo.config(text=atualizado)

janela = tk.Tk()

janela.title('Minha Janela Legal')

janela.config(background="#506155")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

janela.resizable(True, True)

titulo = tk.Label(text='Minha Janela', fg='white',  bg='#506155',font = 120)
titulo.pack()

novo_texto = tk.Entry(text='Digite o novo texto', fg='white',  bg='#506155',)
novo_texto.pack()

butao = tk.Button(text='Botão', fg='white', bg='#506155', command=troca_valor  )
butao.pack()

janela.mainloop()

Atividade 1:

import tkinter as tkExercício #1 - Programa para Restrição de Tráfego por Placa

def checagem():
    numero = novo_texto.get()
    numero = int(numero)
    match numero:
        case 1:
            restricao=("Não Circular 2a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 2:
            restricao=("Não Circular 2a Feira")  
            resposta.config(text=restricao, fg='white', bg='#506155')  
        case 3:
            restricao=("Não Circular 3a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 4:
            restricao=("Não Circular 3a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 5:
            restricao=("Não Circular 4a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 6:
            restricao=("Não Circular 4a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 7:
            restricao=("Não Circular 5a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 8:
            restricao=("Não Circular 5a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 9:
            restricao=("Não Circular 6a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')
        case 0:
            restricao =("Não Circular 6a Feira")
            resposta.config(text=restricao, fg='white', bg='#506155')

janela = tk.Tk()

janela.title('Circulação')
janela.config(background="#506155")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

janela.resizable(True, True)

titulo = tk.Label(text='Digite o ultimo numero do carro:', fg='white',  bg='#506155',font = 120)
titulo.pack()

novo_texto = tk.Entry(text='Digite o ultimo numero aqui', fg='white',  bg='#506155',)
novo_texto.pack()

butao = tk.Button(text='Verificar', fg='white', bg='#506155', command=checagem  )
butao.pack()

resposta = tk.Label(text=" ", fg='white', bg='#506155')
resposta.pack()

janela.mainloop()

#Atividade 2:


import tkinter as tk

#função 

def checagem():
    numero = novo_texto.get()
    numero = int(numero)
    numero1 = novo_texto2.get()
    numero1 = int(numero1)
    match numero:
        case 1:
            match numero1:
                case 1:
                    restricao=("Você gastou R$140,0 comprando a Fraudinha amanteigado")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
                case 2:
                    restricao=("Você gastou R$154,0 comprando a Fraudinha amanteigada")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
        case 2:
             match numero1:
                case 1:
                    restricao=("Você gastou R$130,0 comprando a Picanha a milanesa")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
                case 2:
                    restricao=("Você gastou R$143,0 comprando a Picanha a milanesa")
                    resposta2.config(text=restricao, fg='white', bg='#506155')

        case 3:
            match numero1:
                case 1:
                    restricao=("Você gastou R$120,0 comprando a Costela desfiada")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
                case 2:
                    restricao=("Você gastou R$132,0 comprando a Costela desfiada")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
           
        case 4:
             match numero1:
                case 1:
                    restricao=("Você gastou R$80,0 comprando o Salmão ao molho de pimenta rosa")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
                case 2:
                    restricao=("Você gastou R$88,0 comprando o Salmão ao molho de pimenta rosa")
                    resposta2.config(text=restricao, fg='white', bg='#506155')
#Interface

janela = tk.Tk()

janela.title('Circulação')
janela.config(background="#506155")

janela.geometry("900x600")

janela.maxsize(width=1200, height=900)

janela.minsize(width=400, height=200)

janela.resizable(True, True)

#Menu do restaurante

titulo = tk.Label(text='Digite o numero do prato:', fg='white',  bg='#506155',font = 120)
titulo.pack()
itulo = tk.Label(text='1-Fraudinha amanteigada R$140,0', fg='white',  bg='#506155',font = 120)
itulo.pack()
tulo = tk.Label(text='2-Picanha a milanesa R$130,0', fg='white',  bg='#506155',font = 120)
tulo.pack()
tulo = tk.Label(text='3-Costela desfiada R$120,0', fg='white',  bg='#506155',font = 120)
tulo.pack()
ulo = tk.Label(text='4-Salmão ao molho de pimenta rosa R$80,0', fg='white',  bg='#506155',font = 120)
ulo.pack()

#Entrada da escolha

novo_texto = tk.Entry(text='Digite o numero do prato aqui', fg='white',  bg='#506155',)
novo_texto.pack()

resposta = tk.Label(text=" ", fg='white', bg='#506155')
resposta.pack()

#Menu para gorjeta

titulo2 = tk.Label(text='Você deseja dar a gorjeta de 10% ao garçom:', fg='white',  bg='#506155',font = 120)
titulo2.pack()
itulo2 = tk.Label(text='1-Não', fg='white',  bg='#506155',font = 120)
itulo2.pack()
tulo2 = tk.Label(text='2-Sim', fg='white',  bg='#506155',font = 120)
tulo2.pack()

#Entrada de escolha gorjeta

novo_texto2 = tk.Entry(text='Digite a resposta aqui', fg='white',  bg='#506155',)
novo_texto2.pack()

butao2 = tk.Button(text='Verificar', fg='white', bg='#506155', command=checagem )
butao2.pack()

resposta2 = tk.Label(text=" ", fg='white', bg='#506155')
resposta2.pack()

janela.mainloop()
"""