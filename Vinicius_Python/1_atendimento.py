from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Fila de pessoas")
janela.config(background= "black")

fila = ["Jesus","Vinicius","Ronaldo","Anthony","Erickson"]

def atendimento():
    if fila:
        armazenar = fila.pop(0)
        label2.config(text=f"O cliente {armazenar} foi atendido.", fg= "white")
    else:
        label2.config(text="A fila esta vazia.",fg= "white")


label = Label(text= f"As pessoas que estão na lista são: {fila}", bg= "black", fg= "white")
label.pack(pady= 5)

label1 = Label(text= f"Aperte o botão para começar o atendimento.", bg= "black", fg= "white")
label1.pack(pady= 5)

botao = Button(text= "Começar", command=atendimento, bg= "black", fg= "white")
botao.pack(pady= 5)

label2 = Label(text= " ", bg= "black")
label2.pack(pady= 5)











janela.mainloop()