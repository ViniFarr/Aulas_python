"""
Atividade 1:

for i in range(3):
    for j in range(6):
        print("*", end=" ")
    print()

Atividade 2:

for i in range(1,11):
    for j in range(1,11):
        calculo = i * j
        print(f"{i} X {j} = {calculo}")

Atividade 3:

numero_n = input("Digite o numero de linhas: ")
numero = int(numero_n)

for i in range(1, numero + 1):
    for j in range(1, i + 1):
        print(j, end= ' ')
    print('\n')

Atividade 4:

for i in range(2):
    for j in range(1):
        
        simb = 4
        print(" " + "#" * simb )
        print(simb* "#")

Atividade 5:

num = 1
for i in range (5):
    for j in range (5):
        print(num, end = " ")
        num += 1
    print(" ")

Atividade 6:

numero = 5
meio = 5 // 2
for i in range (meio +1):
    print(" " * (meio - i) + "*" * (2 * i + 1))
    
for i in range(meio -1, -1, -1):
    print(" " * (meio - i) + "*" * (2 * i + 1))

"""