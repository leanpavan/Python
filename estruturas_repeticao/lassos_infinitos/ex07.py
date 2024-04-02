'''
Criar um programa que solicite ao usuário vários números e, ao
digitar 0, calcula a média destes números informados.
'''

soma = 0
contador = 0


while True:
    num = int(input("Digite um número (0 encerra o programa): "))

    if num == 0:
        break

    soma += num
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos números é {media:.2f}")
else:
    print("Nenhum número foi fornecido pelo usuário")
