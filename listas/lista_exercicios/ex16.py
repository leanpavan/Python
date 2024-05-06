'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões.
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um
vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um
total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores
receberam salários nos seguintes intervalos de valores:
a. $200 - $299
b. $300 - $399
c. $400 - $499
d. $500 - $599
e. $600 - $699
f. $700 - $799
g. $800 - $899
h. $900 - $999
i. $1000 em diante
'''
salario_base = 200
vendas_brutas = []
salarios = []
while True:
    valor_bruto = float(input("Digite o valor bruto de vendas do vendedor (-1 para parar): "))
    if valor_bruto == -1:
        break
    else:
        vendas_brutas.append(valor_bruto)

for venda in vendas_brutas:
    comissao = 0.09 * venda
    salarios += [salario_base + comissao]

intervalos = [0] * 9  # Inicializa a lista de contadores com zeros para cada intervalo
for salario in salarios:
    indice = min(8, max(0, (salario - 200) // 100))  # Calcula o índice da lista
    intervalos[int(indice)] += 1

for intervalo in intervalos:
    if intervalo < 8:
        print(f"Intervalo ${200 + intervalo * 100} - ${299 + intervalo * 100}: {intervalo} vendedores")
    else:
        print(f"Intervalo ${1000} em diante: {intervalo} vendedores")

