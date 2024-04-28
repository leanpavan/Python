# Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
vetor = []
soma = 0
multiplicacao = 1

for i in range(5):
    num = int(input(f"Digite o {i+1}º número: "))
    vetor.append(num)

for n in vetor:
    multiplicacao = multiplicacao * n

soma = sum(vetor)

print(vetor)
print(soma)
print(multiplicacao)