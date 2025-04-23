from tkinter import *
janela = Tk()
janela.geometry('900x600')
janela.title("Dados alunos separados Tupla")
janela.config(background= "black")

tupla1 = ("Vinicius", 18, "Varcher")

def verificador():
    nome, idade, curso = tupla1
    
    resposta.config(text=f"O nome do aluno é: {nome} e a idade é {idade} e o curso é {curso}")

introducao = Label(text="Aperte o botão para verificar os dados do aluno", bg="black", fg="white")
introducao.grid(row=0, column=0, sticky="w", columnspan=2)

botao = Button(text="Verificar", command=verificador)
botao.grid(row=0, column=2, padx=40)

resposta = Label(text=" ", bg="black", fg="white")
resposta.grid(row=2, column=0, columnspan=6)

janela.mainloop()