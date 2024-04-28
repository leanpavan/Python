# Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
# elementos do vetor.

a = []
calculo = []
for i in range(10):
    num = int(input(f"Digite o {i+1}º número: "))
    a.append(num)

for n in a:
    quadrado = n**2
    calculo.append(quadrado)

print(f"A soma dos quadrados é {sum(calculo)}")