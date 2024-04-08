'''
4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.
'''

num1 = float(input("Digite o 1ª número: ")) #Menor
num2 = float(input("Digite o 2ª número: "))
num3 = float(input("Digite o 3ª número: "))
num4 = float(input("Digite o 4ª número: "))
num5 = float(input("Digite o 1ª número: ")) #Maior

for _ in range(4):
    if num1 > num2:
        aux = num1
        num1 = num2
        num2 = aux
    if num2 > num3:
        aux = num2
        num2 = num3
        num3 = aux
    if num3 > num4:
        aux = num3
        num3 = num4
        num4 = aux
    if num4 > num5:
        aux = num4
        num4 = num5
        num5 = aux


print(f"\nOs números em ordem crescente são:")
print(num1,num2,num3,num4,num5)

