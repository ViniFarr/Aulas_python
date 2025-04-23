from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Ordenação de Futas Tupla ")
janela.config(background= "black")
tupla1 = (["Banana", "Morango", "Manga", "Jabuticaba", "Limão"])

def ordenacao():
    lista_frutas = tupla1
    lista_frutas.sort()
    resposta.config(text=f"A Lista de fruta: {lista_frutas}")

introducao = Label(text="Aperte o botão para ordenar a Lista de frutas a venda: ", bg= "black" ,fg= "white")
introducao.pack()

botao = Button(text="ordenar", command=ordenacao , bg= "white" ,fg= "black")
botao.pack()

resposta = Label(text= " ", bg= "black" ,fg= "white")
resposta.pack()

janela.mainloop()