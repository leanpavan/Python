'''
8. Elaborar um programa que receba um número em binário, e mostre o seu valor em
decimal.
'''

bin = input("Forneça um número em binário: ")
filtro_bin = '23456789'
iniciar_conversao = False
resultado = 0

for i in range(len(bin)):
    try:
        verificador = bin[i]
        if verificador in filtro_bin and verificador.isdigit():
            print("ERRO! Digite APENAS 1 e 0")
            bin = input("Forneça um número em binário: ")
        else:
            if i == len(bin) - 1:
                iniciar_conversao = True
                print(iniciar_conversao)

    except:
        print("Digite números válidos! 0 e 1")
        bin = input("Forneça um número em binário: ")

while iniciar_conversao:
    for i in range(len(bin)):
        posicao = (i - len(bin) + 1) * -1
        simbolo = int(bin[i])
        soma = simbolo * 2**posicao
        resultado += soma

    print(f"{bin} em decimal é {resultado}")
    break
