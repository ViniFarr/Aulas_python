from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Contagem no Tupla")
janela.config(background= "black")
tupla1 = ("Abacate", "Cereja", "Pera", "Kiwi", "Framboesa")

def contador():
    contar = tupla1.count("Maçã")
    resposta.config(text=f"A quantidade de Maçãs que tem é de: {contar}")


introducao = Label(text="Aperte no botão para contar quantas Maçãs tem na Lista", bg="black", fg="white")
introducao.pack()

botao = Button(text="Contar", command=contador)
botao.pack()

resposta = Label(text=" ", bg="black", fg="white")
resposta.pack()
 
janela.mainloop()
 