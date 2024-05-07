'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se
seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo
'''



def caractere(texto):
    p = 0
    for letra in texto:
        if letra == "P" or letra == 'p':
            p += 1
    if p > 0:
        return p


text = input("Digite um texto: ")
print("Número de caracteres 'P':", caractere(text))
