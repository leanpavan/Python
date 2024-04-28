# Faça um Programa que leia 4 notas, mostre as notas e a média na tela
notas = []

for i in range(4):
    nota = int(input("Digite a nota: "))
    notas.append(nota)

media = sum(notas) / len(notas)
print(f"A média das {notas} é {media:.2f}")