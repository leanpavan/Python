'''
Criar um programa que pede ao usuário 5 números, e informa
qual é o menor e qual é o maior deles.
'''

for i in range(5):
    num = int(input(f"Informe o {i + 1}º número: "))
    if i == 0:
        maior = num
        menor = num
    if num >= maior:
        maior = num
    if num <= menor:
        menor = num

print(f"O maior número é {maior}")
print(f"O menor número é {menor}")