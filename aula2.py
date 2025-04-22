"""
======================================Atividade1:===============================================================

valor_retangulo = input("Digite o valor da largura do retângulo em cm: ")
valor_altura = input("Digite o valor da altura do retângulo em cm: ")
resultado = int(valor_retangulo) * int(valor_altura)
print(f"A área do retângulo é de: {resultado}cm ")


======================================Atividade2:==================================================

numero = input(f"Escreva o numero que sera calculado: ")
resultado_dobro = int(numero) * 2
resultado_triplo = int(numero) * 3
print(f"O valor {numero} dobrado é {resultado_dobro} e o valor triplicado é de {resultado_triplo}")

======================================Atividade3:===========================================================

valor = input("Digite o valor para saber se é impar ou par: ")
if(int(valor)% 2 == 0):
    print("é par")
else:
    print("é impar")

======================================Atividade4:=========================================================

valor_primeiro = input("Digite a primeira nota: ")
valor_segundo = input("Digite a segundo nota: ")
valor_terceiro = input("Digite a terceiro nota: ")
valor_quarto = input("Digite a quarto nota: ")
resultado = float(valor_quarto) + float(valor_primeiro) + float(valor_segundo) + float(valor_terceiro)
media = float(resultado) / 4
if(media < 5):
    print(f"Sinto muito você foi reprovado com a média de: {media} mais sorte na proxima vez")
elif(media < 7):
    print(f"Atenção você esta proximo de reprovar pois você esta em recuperação com a média de: {media}")
else:
    print(f"Parabéns você foi aprovado com a média de: {media}")

=====================================Atividade5:============================================================

quantidade = input("Digite a quantidade do produto selecionado: ")
valor_unitario = input("Digite o valor unitario do produto: ")
valor_sem_desconto = int(quantidade) * int(valor_unitario)
if(int(quantidade) > 10):
    desconto = float(valor_sem_desconto) * 0.1
    valor_com_desconto = float(valor_sem_desconto) - float(desconto)
    print(f"O valor é de {valor_com_desconto}")
else:
    print(f"O valor é de {valor_sem_desconto}")

=====================================Atividade6:=================================================

pergunta = input("Informe o último número da placa do seu carro: ")
if(pergunta == "1"):
    print("Você não podera circular com o carro na Segunda-Feira")
elif(pergunta == "2"):
    print("Você não podera circular com o carro na Terça-Feira")
elif(pergunta == "3"):
    print("Você não podera circular com o carro na Quarta-Feira")
elif(pergunta == "4"):
    print("Você não podera circular com o carro na Quinta-Feira")
elif(pergunta == "5"):
    print("Você não podera circular com o carro na Sexta-Feira")
elif(pergunta == "6"):
    print("Você não podera circular com o carro na Segunda-Feira")
elif(pergunta == "7"):
    print("Você não podera circular com o carro na Terça-Feira")
elif(pergunta == "8"):
    print("Você não podera circular com o carro na Quarta-Feira")
elif(pergunta == "9"):
    print("Você não podera circular com o carro na Quinta-Feira")
elif(pergunta == "0"):
    print("Você não podera circular com o carro na Sexta-Feira")
else:
    print("Não foi possivel achar a placa, Verifique se você colocou apenas um numero e que ele é o ultimo da placa")

=====================================Atividade7:================================================================================

distancia_percorrida = input("Informe a distancia percorrida na viajem em quilometros: ")
valor_da_gasolina = input("Informe o valor da gasolina por litro: ")
gasto_combustivel = input("Informe o consumo de gasolina por quilometro: ")
quantidade_combustivel = int(distancia_percorrida) * int(gasto_combustivel)
valor_total = int(quantidade_combustivel) * int(valor_da_gasolina)
print(f"O valor gasto é de: {valor_total}")

====================================Atividade8:============================================================================================

salario_fixo = input("Informe o seu salario fixo: ")
venda = input("Informe o valor da venda realizada: ")
bonus = float(venda) * 0.04
salario_total = float(salario_fixo) + float(bonus)
print(f"O valor de comissão que você arrecadou foi de {bonus} e seu salario fixo é de {salario_fixo} totalizando {salario_total}")
"""

    