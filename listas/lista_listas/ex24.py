'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os resultados em
um vetor . Depois, mostre quantas vezes cada valor foi conseguido. Dica: use um vetor de contadores(1-6) e uma
função para gerar numeros aleatórios, simulando os lançamentos dos dados.
'''
import random

dados = []

#Lançamento dos dados
for i in range(100):
    dados.append(random.randint(1,6))

for c in range(1,7):
    print(f"O valor {c} caiu {dados.count(c)} vezes")