'''
6. Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome.
'''

nome_completo = input("Digite seu nome completo: ")

print(nome_completo)
primeiro_nome = ''
ultimo_nome = ''

i = 0
while i < len(nome_completo):
    if nome_completo[i] != "":
        primeiro_nome += nome_completo[i]
    else:
        break
    i += 1
i += 1


print(primeiro_nome)