'''
4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.
'''

num1 = float(input("Digite o 1ª número: ")) #Menor
num2 = float(input("Digite o 2ª número: "))
num3 = float(input("Digite o 3ª número: "))
num4 = float(input("Digite o 4ª número: "))
num5 = float(input("Digite o 1ª número: ")) #Maior
ordem = True
while ordem:
    ordem = False
    if num1 > num2:
        num1, num2 = num2, num1
        ordem = True
    if num2 > num3:
        num2, num3 = num3, num2
        ordem = True
    if num3 > num4:
        num3, num4 = num4, num3
        ordem = True
    if num4 > num5:
        num4, num5 = num5, num4
        ordem = True

print(f"\nOs números em ordem crescente são:")
print(num1,num2,num3,num4,num5)

