'''
7. Elaborar um programa que solicita várias palavras ao usuário, sendo que o critério de
parada é digitar uma palavra vazia. Contar e exibir quantas letras A existem neste
conjunto de palavras.
'''

a_count = 0

while True:
    word = input("Digite uma palavra: ")

    for l in word:
        if l == "a":
            a_count += 1

    if word == '':
        break

print(f"\nExiste {a_count} letras A nas palavras digitadas")