'''
#Estudo par ou ímpar
#Escreva um programa que solicite um número ao usuário e, em seguida, determine se esse número é par ou ímpar.

num = int(input("Forneça um número: "))

if num % 2 == 0:
    print(f"O número {num} é par!!")
else:
    print(f"O número {num} é ímpar!!")
'''

'''
#Exercício de Tabuada:
#Escreva um programa que peça ao usuário para inserir um número e, em seguida, exiba a tabuada desse número de 1 a 10.

num = int(input("Forneça um número: "))

for i in range(1,11):
    tabuada = num * i
    print(tabuada)
'''

# Exercício de Verificação de Números Primos:
# Escreva um programa que verifique se um número fornecido pelo usuário é primo ou não.

num = int(input("Forneça um número: "))
primo = True

if num < 2:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break

if primo:
    print(f"O número {num} é primo")
else:
    print(f"O número {num} não é primo")

'''
#Escreva um programa que solicite um número ao usuário e calcule a soma de todos os números de 1 até esse número.

num = int(input("Forneça um número: "))
soma = 0

for i in range(1, num + 1):
    soma += i

print(soma)
'''

'''
#Escreva um programa que conte e exiba quantos dígitos possui um número fornecido pelo usuário.

num = input("Forneça um número: ")
digitos = 0

for n in num:
    digitos += 1

print(digitos)
'''

