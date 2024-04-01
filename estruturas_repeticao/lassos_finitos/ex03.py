'''
Criar um programa que recebe um texto digitado pelo usuário e
o imprime apenas com consoantes, removendo as vogais. Obs.:
desconsiderar letras maiúsculas e acentos.
'''

resultado = ""

frase = input("Digite umaa frase: ")

for i in range(len(frase)):
    if frase[i] != "a" and frase[i] != "e" and frase[i] != "i" and frase[i] != "o" and frase[i] != "u":
        resultado += frase[i]

print(f"A frase sem vogais fica {resultado}")