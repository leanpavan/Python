'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
'''



def iterador(num):
    digitos = len(str(num))
    return digitos

num = int(input("Digite um número: "))
digitos = iterador(num)
print(f"Número de dígitos: {digitos}")

