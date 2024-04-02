'''
Escreva um programa em Python que gera números entre 1000 e 1999 e mostra aqueles
que divididos por 11 dão resto 5.
'''

for i in range(1000,2000):
    num = i
    if num % 11 == 5:
        print(num)