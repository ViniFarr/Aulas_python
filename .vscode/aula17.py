import tkinter as tk

import time
janela = tk.Tk()
lista = ["Jesus", "Vinicius", "Daniel", "Amadeu", "Douglas", "Matheus", "Tiago"]

def verificar():
    entrada = escrita.get()

    match entrada:
        case "1":
            for nome in lista:     
                Listbox.insert(tk.END,nome)
                time.sleep(0.3)

        case "2":  
            resposta2 = tk.Label(text="flw")
            resposta2.pack()

janela.title('Calculo')
janela.config(background="black") 

introducao = tk.Label(text = "Escolha a opção que desejar: ")
introducao.pack()

introducao2 = tk.Label(text = "1 - Para percorrer a lista ")
introducao2.pack()

introducao3 = tk.Label(text = "2 - Para nem começar ")
introducao3.pack()

introducao4 = tk.Label(text = "Digite o numero correspondente a opção:  ")
introducao4.pack()

escrita = tk.Entry()
escrita.pack()

botao = tk.Button(text= "CONFIRMAR" , command=verificar)
botao.pack()

Listbox = tk.Listbox(janela)
Listbox.pack()

janela.mainloop()






