"""
Atividade 1

n = input("Digite o numero: ")
ni = int(n)
a = 0
b = 1

for _ in range (ni):
    print(a, end=' ')
    a , b = b , a + b
   
Atividade 4

frase = input("Digite a frase: ")
contadora = 0

for i in frase:
    if("a" <= i <= "z" ) or ("A" <= i <= "Z"):
        contadora += 1

print(f"O numero de letras é de: ")
      
Atividade 10

numero_n = input("Digite o numero de linhas: ")
numero = int(numero_n)
for i in range(1, numero + 1):
    espaco = numero - i
    simb = 2 * i - 1
    print(" " * espaco + "*" * simb )

Atividade 2

numero_n = 3
for i in range(1, 30):
    if(int(i % numero_n == 0)):
        print(i)
    else:
        continue

Atividade 3
"""
soma = 0
numero_divisor = 2
for i in range(1, 50):
    if(int(i % numero_divisor != 0)):
        soma = soma + i
        print(f"Soma é de: ",soma)
    else:
        continue
        



       
