'''
4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.
'''

numeros = []
num_ord = 0

for i in range(5):
    num = int(input("Digite um número: "))

    numeros.append(num)
    num_ord = sorted(numeros)

print(num_ord)

