# Criar um programa que solicite ao usuário 2 listas com 5
# elementos cada. Como resultado, criar uma terceira lista que
# intercala os elementos das duas listas.

lista1 = []
lista2 = []
lista3 = []

for n in range(5):
    num1 = int(input("bota um numero ae: "))
    num2 = int(input("bota outro numero ae: "))
    lista1.append(num1)
    lista2.append(num2)

    lista3.append(lista1[n])
    lista3.append(lista2[n])

print(lista3)