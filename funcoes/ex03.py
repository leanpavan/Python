'''
Criar um programa que receba uma lista de números e retorne a
média dos mesmos.
'''


def calcular_media(nums):
    media = sum(nums) / len(nums)
    return media


lista_nums = []
while True:
    num = int(input("Digite um número (Digite -1 para parar): "))
    if num == -1:
        break
    else:
        lista_nums.append(num)

media = calcular_media(lista_nums)
print(media)