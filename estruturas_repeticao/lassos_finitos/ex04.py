'''
Criar um programa que solicita um número ao usuário e exibe a
tabuada deste número de 1 a 10, no formato:
'''

num = int(input("Digite um número de 1 a 10: "))

for i in range(10):
    if num > 10 and num < 1:
        break
    else:
        tabuada = num * (i+1)
        print(f"{num} * {i+1} = {tabuada}")