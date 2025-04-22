import tkinter as tk

janela = tk.Tk()

janela.title('Aproveite+')
janela.config(background="#00513f") 

introducao = tk.Label(text = "Aproveite+",font=('Georgia',45), bg="#00513f", fg="#42f5ef")
introducao.pack(pady=(500,0))

introducao2 = tk.Label(text = "Email:",font=('Georgia',12), bg="#00513f", fg="#42f5ef")
introducao2.pack(side="left",padx=(800,0))

introducao3 = tk.Label(text = "Senha:",font=('Georgia',12), bg="#00513f", fg="#42f5ef")
introducao3.pack(side="bottom",padx= (0,1050))

janela.mainloop()