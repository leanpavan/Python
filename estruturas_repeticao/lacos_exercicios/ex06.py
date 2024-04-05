'''
6. Elaborar um programa que receba o nome completo do usuário, e imprima apenas o
primeiro e último nome.
'''

full_name = input("Digite seu nome completo: ")
first_name = ''
last_name = ''

espaco = False

for l in full_name:
    if l == " ":
        espaco = True
    if l == " ":
        last_name = ""
    if espaco == True:
        last_name += l
    else:
        first_name += l


print(f"\n{first_name}{last_name}")

