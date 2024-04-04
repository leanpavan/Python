'''
4. Peça 5 números ao usuário. Fazendo uso de laços, organize e mostre eles em ordem
crescente.
'''

num = 0
maior = 0
segundo = 0
terceiro = 0
quarto = 0
menor = 0

for i in range(5):
    num = int(input(f"Digite o {i + 1} número: "))
    if i == 0:
        maior = num
        menor = num

    if i == 1:
        if num > maior:
            maior = num
        else:
            menor = num

    if i == 2:
        if num > maior:
            segundo = maior
            maior = num
        elif num > menor:
            segundo = num
        elif num < menor:
            quarto = menor
            menor = num

    if i == 3:
        if num > maior:
            terceiro = segundo
            segundo = maior
            maior = num
        elif num > segundo:
            terceiro = segundo
            segundo = num
        elif num > menor and num > quarto:
            terceiro = num
        elif num < menor:
            quarto = menor
            terceiro = quarto
            menor = num
        elif num < quarto:
            terceiro = quarto
            quarto = num

        if i == 4:
            if num > maior:
                quarto = terceiro
                terceiro = segundo
                segundo = maior
                maior = num
            elif num > segundo:
                quarto = terceiro
                terceiro = segundo
                segundo = num
            elif num > terceiro:
                quarto = terceiro
                terceiro = num
            elif num < menor:
                quarto = menor
                menor = num
            else:
                quarto = num

    print(f"\n{menor},{quarto},{terceiro},{segundo},{maior}")

