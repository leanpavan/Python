'''
9. Elaborar um programa em Python que converta um número decimal em hexadecimal,
fazendo uso do método de divisões sucessivas.
'''

dec = int(input("Digite um número em decimal: "))
dec_original = dec
hex_characters = "0123456789ABCDEF"
hex = ''

while dec > 0:
    resto = dec % 16
    hex = hex_characters[resto] + hex
    dec //= 16

print(f"\nO número {dec_original} em hexadecimal é: {hex}")
