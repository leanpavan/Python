# Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

vetor1 = []
vetor2 = []
vetor3 = []
vetor_intercalado = []

for i in range(10):
    num = int(input(f"Digite o {i + 1}º número da 1º lista: "))
    vetor1.append(num)

for c in range(10):
    num2 = int(input(f"Digite o {c + 1}º número da 2º lista: "))
    vetor2.append(num2)

for n in range(10):
    num3 = int(input(f"Digite o {n + 1}º número da 3º lista: "))
    vetor3.append(num3)

for j in range(len(vetor1)):
    vetor_intercalado.append(vetor1[j])
    vetor_intercalado.append(vetor2[j])
    vetor_intercalado.append(vetor3[j])

print(vetor_intercalado)