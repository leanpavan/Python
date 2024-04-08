'''
9. Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso do método de divisões sucessivas.
'''

dec = int(input("Digite um número em decimal: "))
divisor = 16
checker = ''
hex = ''
resto = ''
resultado = dec

if dec < divisor:
    hex = "0123456789ABCDEF"[dec]
else:
    while True:
        resultado //= divisor
        resto = dec % divisor
        if resultado > 15:
            hex  = "0123456789ABCDEF"[resto] + hex
        else:
            hex = "0123456789ABCDEF"[resultado] + "0123456789ABCDEF"[resto] + hex
            break

print(f"\nO número {dec} decimal equivale a {hex} hexadecimal")

