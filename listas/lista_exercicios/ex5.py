# Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor
# PAR e os números IMPARES no vetor impar. Imprima os três vetores.

vetor = []
par = []
impar = []

for i in range(20):
    num = int(input("Digite um número: "))
    vetor.append(num)

for n in vetor:
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)

print(vetor)
print(f"Os pares são: {par}")
print(f"Os pares são: {impar}")