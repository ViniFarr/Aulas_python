from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Verificação de Frutas Tupla")
janela.config(background= "black")
tupla1 = ("Laranja", "Bergamota", "Inga", "Figo", "Caqui")

def verificar():
    if ("Banana" in tupla1) == False:
        resposta.config(text="Banana não esta no texto")
    elif ("Banana" in tupla1) == True:
        resposta.config(text="Banana esta no texto")

introducao = Label(text="Aperte no botão para verificar se a fruta Banana esta na Lista", bg="black", fg="white")
introducao.pack()

botao = Button(text="Verificar", command=verificar )
botao.pack()

resposta = Label(text=" ", bg= "black", fg="white")
resposta.pack()

janela.mainloop()