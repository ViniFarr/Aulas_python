"""Atividade 1

numero = input("Digite o numero para descobrir se é impar ou par: ")
if(int(numero) % 2 == 0):
    print("É par")
else:
    print("É impar")

   ATIVIDADE 2

numero1 = input("Informe o primeiro numero: ")
numero2 = input("Informe o segundo numero: ")
if(int(numero1) > int(numero2)):
    print(f"O numero {numero1} é maior do que o numero {numero2}")
elif(int(numero2) > int(numero1)):
    print(f"O numero {numero2} é maior do que o numero {numero1}")
else:
    print(f"O numero {numero1} é o mesmo do numero {numero2} ")

Atividade 3

valor_inicial = input("Informe o valor das suas compras para verificar descontos: ")
if(float(valor_inicial) >= 100.00):
    desconto = float(valor_inicial) * 0.10
    valor_total = float(valor_inicial) - desconto 
    print(f"O valor com os descontos é de: {valor_total}")
elif(float(valor_inicial) >= 50.00):
    desconto = float(valor_inicial) * 0.05
    valor_total = float(valor_inicial) - desconto 
    print(f"O valor com os descontos é de: {valor_total}")
else:
    print(f"Não foi possivel encontrar descontos disponiveis o valor é de: {valor_inicial}")

Atividade 4

idade = input("Informe a idade para a verificação: ")
if(int(idade) >= 18 ):
    print("Você é de maior")
else:
    print("Você é de menor")

Atividade 5

numero = input("Informe o numero para a verificação: ")
if(int(numero) > 0):
    print("É positivo")
elif(int(numero) == 0):
    print("É um zero")
else:
    print("É negativo")

Atividade 6

nota1 = input("Informe a nota para o calculo da media: ")
nota2 = input("Informe a segunda nota para a calculo da media: ")
nota_total = int(nota1) + int(nota2)
media = int(nota_total) / 2
print(f"A sua media é de: {media}")
if(media >= 7):
    print("Aprovado, parabens")
elif(media >= 5):
    print("Você esta em recuperação, cuidado")
else:
    print("Reprovado, tente na proxima vez")

Atividade 7

numero1 = input("Informe o valor para o calculo: ")
operacao = input("Informe a operação para o calculo: ")
numero2 = input("Informe o valor para o calculo: ")

if(operacao == "+"):
    resultado = int(numero1) + int(numero2)
    print(f"O resultado é: {resultado}")
elif(operacao == "-"):
    resultado = int(numero1) - int(numero2)
    print(f"O resultado é: {resultado}")
elif(operacao == "*"):
    resultado = int(numero1) * int(numero2)
    print(f"O resultado é: {resultado}")
elif(operacao == "/"):
    if(int(numero1) == 0 or int(numero2) == 0):
        print("ERRO")
    else:
        resultado = float(numero1) / float(numero2)
        print(f"O resultado é: {resultado}")
else:
    print("Não foi possivel realizar o calculo")

Atividade 8

numero1 = input("Informe um dos lados do triangulo: ")
numero2 = input("Informe o outro lado do triangulo: ")
numero3 = input("Informe o outro lado do triangulo: ")
if(int(numero1) == int(numero2) == int(numero3)):
    print("O triangulo é um triangulo equilatero")
elif(int(numero1) == int(numero2) or int(numero2) == int(numero3) or  int(numero1) == int(numero3) ):
    print("É um triangulo isoceles")
else:
    print("É um triangulo escaleno")

Atividade 9

numero1 = input("Informe o primeiro numero para ver se ele é mutiplo do segundo numero: ")
numero2 = input("Informe o segundo numero: ")
if(int(numero1) % int(numero2) == 0 ):
    print(f"O numero {numero1} é mutiplo do numero: {numero2}")
else:
    print(f"O numero {numero1} não é o mutiplo do numero: {numero2}")

Atividade 10

graus_c = input("Informe o graus em celcios para a converção: ")
covercao = input("Informe para qual você vai converter (F) para fahrenheit e (K) para kelvin: ")
if(covercao == "F" or covercao == "f" ):
    calculo = float(graus_c) * 1.8 + 32
    print(f"A temperatura em Fahrenheit é de: {calculo}")
elif(covercao == "K" or covercao == "f" ):
    calculo = float(graus_c) + 273.15
    print(f"A temperatura em Kelvin é de: {calculo}")
"""