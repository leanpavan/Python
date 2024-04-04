'''
5. Dado um país A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano,
e um país B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever
um programa em Python que seja capaz de calcular e iterativamente e no fim imprimir o
tempo necessário para que a população do país A ultrapasse a população do país B.
'''

a = int(5000000)
b = int(7000000)
ano = 0
while a < b:
    ano += 1
    a_natalidade = a * 0.03
    b_natalidade = b * 0.02
    a += a_natalidade
    b += b_natalidade

print(f"População de A: {int(a)}")
print(f"População de B: {int(b)}")
print(f"Após {ano} anos")