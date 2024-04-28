# Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
# valores deverão ser compostos pelos elementos intercalados dos dois outros vetores

vetor1 = []
vetor2 = []
vetor_intercalado = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número da 1º lista: "))
    vetor1.append(num)

for c in range(10):
    num2 = int(input(f"Digite o {c + 1}º número da 2º lista: "))
    vetor2.append(num2)

for j in range(len(vetor1)):
    vetor_intercalado.append(vetor1[j])
    vetor_intercalado.append(vetor2[j])

print(vetor_intercalado)