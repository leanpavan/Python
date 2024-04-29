'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto,
calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas
ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
'''

temps = []
meses = ['Janeiro', 'Feveiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for mes in meses:
    temp = float(input(f"Qual a temperatura de {mes}? "))
    temps.append(temp)
media = sum(temps) / len(temps)
print(f"\nMédia das temperaturas: {media:.2f}\n")
for i in range(len(temps)):
    if temps[i] > media:
        print(meses[i], temps[i], "ºC")