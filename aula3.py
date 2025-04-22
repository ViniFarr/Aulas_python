"""
Atividade 1:

valor = float(input("Digite o valor total das suas compras: "))
if(valor >= 500.0):
    desconto = valor * 0.1
    valor_total = valor - desconto
    print(f"O valor total das suas compras é de {valor_total} reais porque você ganhou um desconto de {desconto} reais")
elif(valor >= 200.0 and valor <= 499.9):
    desconto = valor * 0.05
    valor_total = valor - desconto
    print(f"O valor total das suas compras é de {valor_total} reais porque você ganhou um desconto de {desconto} reais")
else:
    print(f"Sinto muito você não atingiu o valor para o desconto então o valor das suas compras é de {valor} reais")

Atividade 2:

galinhas = int(input("Digite a quantia de frangos para calcular o valor: "))
custo = 11
custo_total = custo * galinhas
print(f"Esse sera a quantia em reais necessarios para implantar tudo nas galinhas: {custo_total} reais")

Atividade 3:

quantidade_sanduiche = float(input("Informe a quantidade de sanduiche para o calculo: "))
queijo_total = 100 * quantidade_sanduiche
presunto_total = 50 * quantidade_sanduiche
hamburguer_total = 100 * quantidade_sanduiche
kg_queijo = 0.001 * queijo_total
kg_presunto = 0.001 * presunto_total
kg_hamburguer = 0.001 * hamburguer_total
print(f"A quantia em quilos de hambúrguer é: {kg_hamburguer}kg ")
print(f"A quantia em quilos de queijo é: {kg_queijo}kg")
print(f"A quantia em quilos de presunto é: {kg_presunto}kg")

Atividade 4:

quantidade_grande = int(input("Informe a quantidade de camisetas grandes: "))
quantidade_medio = int(input("Informe a quantidade de camisetas medio: "))
quantidade_pequeno = int(input("Informe a quantidade de camisetas pequeno: "))
custo_grande = 15 * quantidade_grande 
custo_medio = 12 * quantidade_medio
custo_pequeno = 10 * quantidade_pequeno
custo_total = custo_grande + custo_medio + custo_pequeno
print(f"O valor total é de: {custo_total}R$")

Atividade 5:

ano = int(input("Qual é o ano para a verificação: "))
if(ano % 4 == 0 ):
    print("esse ano é bissesto")
else:
    print("esse ano não é bissesto")
    
"""