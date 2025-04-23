from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Juntar duas Tupla")
janela.config(background= "black")
tupla1 = ("Banana", "Morango")
tupla2 = ("Manga", "jabuticaba", "Limão")
def juntar():
    tupla3= tupla1 + tupla2
    resposta.config(text=f"A Lista de fruta: {tupla3}")

introducao = Label(text="Aperte o botão para juntar as duas listas: ", bg= "black" ,fg= "white")
introducao.pack()

botao = Button(text="Juntar", command=juntar , bg= "white" ,fg= "black")
botao.pack()

resposta = Label(text= " ", bg= "black" ,fg= "white")
resposta.pack()

janela.mainloop()