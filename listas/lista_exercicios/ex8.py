# Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
# Imprima a idade e a altura na ordem inversa a ordem lida.

idades = []
alturas = []

for i in range(5):
    idade = int(input(f"Digite a idade da {i+1}º pessoa: "))
    altura = int(input(f"Digite a altura da {i + 1}º pessoa em centímetros: "))
    idades.append(idade)
    alturas.append(altura)

alturas.reverse()
idades.reverse()

print(idades)
print(alturas)