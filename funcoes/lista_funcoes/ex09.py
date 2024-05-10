'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127
-> 721.
'''


def inverter(n):
    aux = ''
    for i in n:
        aux = i + aux
    print(f"{n} -> {aux}")

while True:
    num = input("Digite um número (-1 - Finaliza): ")
    if num == '-1':
        break
    inverter(num)