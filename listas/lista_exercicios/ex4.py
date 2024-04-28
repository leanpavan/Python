# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as
# consoantes.
caracteres = []
vogais = 'aeiou'
consoantes = []
for i in range(10):
    carac = input("Digite um caracter: ").lower()
    caracteres.append(carac)

for c in caracteres:
    if c not in vogais:
        consoantes.append(c)

print(f"As consoantes são {consoantes}")