# Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
vetor = []
for i in range(10):
    num = int(input("Digite um número: "))
    vetor.append(num)

vetor.reverse()
print(vetor)