'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se
seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
'''


def contador(n):
    if n > 0:
        return 'P'
    if n < 0:
        return 'N'


while True:
    num = int(input("Digite um número (Digite -0 para parar): "))
    if num == -0:
        break
    resultado = contador(num)

    print(f"O número {num} é {resultado}")
