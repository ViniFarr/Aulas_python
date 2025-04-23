from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Somarvalores")
janela.config(background= "black")

tupla1 = (5, 10, 12, 15)

def calcular():
    somar1, somar2, somar3, somar4 = tupla1
    somar = somar1 + somar2 + somar3 + somar4
    resposta.config(text=f"A soma da lista é de: {somar}")

introducao = Label(text="Aperte o botão para o somar os valores", bg="black", fg="white")
introducao.grid(row=0, column=0, sticky="w", columnspan=2)

botao = Button(text="Somar", command=calcular)
botao.grid(row=0, column=2, padx=40)

resposta = Label(text=" ", bg="black", fg="white")
resposta.grid(row=2, column=0, columnspan=6)

janela.mainloop()