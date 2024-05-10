'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três
argumentos.
'''


def soma(arg1, arg2, arg3):
    return arg1 + arg2 + arg3

arg1 = int(input('Digite o primeiro valor: '))
arg2 = int(input('Digite o segundo valor: '))
arg3 = int(input('Digite o terceiro valor: '))
print(soma(arg1, arg2, arg3))