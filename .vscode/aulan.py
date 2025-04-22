fila = []

while True:
    print("\n1 - Adicionar Cliente")
    print("2 - Atender Cliente")
    print("3 - Ver Fila")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        fila.append(nome)
        print(f"{nome} entrou na fila.")

    elif opcao == "2":
        if fila:
            atendido = fila.pop(0)
            print(f"{atendido} foi atendido.")
        else: 
            print("A fila ta vazia.")
    
    elif opcao == "3":
        print(f"Fila atual: {fila}.")
    elif opcao == "4":
        break
    else:
        print("Opção invalida.")
