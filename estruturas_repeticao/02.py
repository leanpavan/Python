'''
Elaborar um progama que calcula o fatorial de um número qualquer
5! = 5 * 4 * 3 * 2 * 1
'''

fat = 1
num = int(input("Digite um número: "))

for i in range(num, 1, -1):
    fat *= i

print(f"O fatorial de {num} é {fat}")