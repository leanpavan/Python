'''
Criar um programa que pede dois números ao usuário. O
primeiro será o numerador, e o segundo será o expoente. A saída
do programa deve ser o resultado da operação numerador
elevado a expoente. Obs.: não usar função interna que calcula
automaticamente potência.
'''

numerador = int(input("Digite o numerador: "))
expoente = int(input("Digite o expoente: "))
resultado = 0

for i in range(1, expoente):
    resultado += numerador**2

print(resultado)