from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Adicionar na fila")
janela.config(background= "black")

fila = []

def adicionar():
    nome = entrada.get()
    if nome.lower().strip() != "sair":
        fila.append(nome)
        entrada.delete(0, END)
    else:
        resultado.config(text=f"Dentro da lista esta: {fila}", fg="white")

label = Label(text= f"Digite para adicionar os nomes e aperte o botão: ", bg= "black", fg= "white")
label.pack(pady= 5)

entrada = Entry()
entrada.pack(pady= 5)

botao = Button(text="ADICONAR", command=adicionar ,bg= "white", fg= "black")
botao.pack(pady= 5)

resultado = Label(text= " ", bg= "black" )
resultado.pack(pady= 5)

janela.mainloop()

