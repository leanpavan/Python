'''
Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados.
'''

while True:
    try:
        num = int(input("Digite um número: "))
        if num == 0:
            break
    except:
        media
