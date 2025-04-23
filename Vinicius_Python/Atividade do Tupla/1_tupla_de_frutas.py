from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Tupla de Frutas")
janela.config(background= "black")
tupla1 = ("Banana", "Morango", "Manga", "jabuticaba", "Limão")

def ver():
    resposta.config(text=f"A Lista de fruta: {tupla1}")

introducao = Label(text="Aperte o botão para ver a Lista de frutas a venda: ", bg= "black" ,fg= "white")
introducao.pack()

botao = Button(text="Ver", command=ver , bg= "white" ,fg= "black")
botao.pack()

resposta = Label(text= " ", bg= "black" ,fg= "white")
resposta.pack()

janela.mainloop()