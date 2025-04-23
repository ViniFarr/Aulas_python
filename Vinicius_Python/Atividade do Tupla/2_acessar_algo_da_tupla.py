from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Acessar conteudo Tupla")
janela.config(background= "black")

tupla1 = ("Lima", "Maracuja", "Tamaringo", "Amora", "Maçã")

def acessar():
    resposta.config(text=f"A terceira fruta é {tupla1[2]}")

tupla_lista = Label(text=tupla1, bg= "black", fg= "white")
tupla_lista.pack()

introducao = Label(text=f"Aperte no botão para aessar a terceira fruta da lista",bg= "black", fg= "white")
introducao.pack()

botao = Button(text="Acessar", command= acessar)
botao.pack()

resposta = Label(text=" ", bg= "black", fg= "white")
resposta.pack()
 
janela.mainloop()
 