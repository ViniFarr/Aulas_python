from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Pegar senha")
janela.config(background= "black")

fila = []
def senha():
    nome = entrada.get()
    fila.append(nome)
    for i in range (1,len(fila)+1):
        resultado.config(text=f"O cliente {nome} pegou a senha {i}")

introducao = Label(text= "Digite o nome para pegar a senha: ", bg= "black", fg= "white")
introducao.pack(pady= 5)

entrada = Entry()
entrada.pack(pady= 5)

botao = Button(text= "Pegar Senha", command= senha, bg= "black", fg= "white")
botao.pack()

resultado = Label(text= " ", bg= "black", fg= "white")
resultado.pack(pady= 5)

janela.mainloop()