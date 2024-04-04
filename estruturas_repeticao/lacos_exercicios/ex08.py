'''
8. Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal.
'''

bin = input("Forneça um número em binário: ")
dec = 0

for i in range(len(bin)):
    posicao = (i - len(bin) + 1) * -1
    simbulo = int(bin[i])
    soma = simbulo * 2**posicao
    dec += soma
print(dec)