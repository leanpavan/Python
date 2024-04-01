'''
9. Implementar um programa que valide um CPF. Para tanto, solicitar em separado cada
um dos 11 dígitos do CPF.
'''

#529.982.247-25

#Solicitar o CPF
i, ii, iii, iv, v, vi, vii, viii, ix, x, xi = map(int, input("Digite os 11 números do CPF separados por espaço (somento números): ").split())

#Validação do primeiro dígito
passo1 = i * 10 + ii * 9 + iii * 8 + iv * 7 + v * 6 + vi * 5 + vii * 4 + viii * 3 + ix * 2
primeiro_digito = passo1 * 10 % 11

#Validação do segundo dígito
passo2 = i * 11 + ii * 10 + iii * 9 + iv * 8 + v * 7 + vi * 6 + vii * 5 + viii * 4 + ix * 3 + x * 2
segundo_digito = passo2 * 10 % 11

#Verificar se o CPF é válido
if primeiro_digito == x and segundo_digito == xi:
    print(f"O CPF {i}{ii}{iii}{iv}{v}{vi}{vii}{viii}{ix}-{x}{xi} é válido")
else:
    print(f"O CPF {i}{ii}{iii}{iv}{v}{vi}{vii}{viii}{ix}-{x}{xi} é inválido")