'''
Criar um programa que solicita ao usuário 10 números, contando
quantos são pares e quantos são ímpares. Informar ao final estas
informações.
'''

pares = 0
impares = 0

for i in range(10):
    num = int(input(f"Digite o {str(i+1)}º número: "))
    result = num % 2
    if result == 0:
        print(f"O número {num} é par")
        pares += 1
    else:
        print(f"O número {num} é ímpar")
        impares += 1

print(f"Há {pares} números pares e {impares} número ímpares")