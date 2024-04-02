'''
1. Um determinado material radioativo perde metade de sua massa a cada 50 segundos.
Dada a massa inicial, em gramas, fazer um algoritmo que determine o tempo necessário
para que a massa se torne menor do que 0,5 grama. Imprima como dado de saída a massa
final e o tempo calculado em segundos.
'''

massa = float(input("Digite a massa inicial do material radioativo em gramas: "))
tempo = 0
massa_final = 0.5

while massa > massa_final:
    print(massa, "g")
    massa = massa / 2
    tempo += 50

print(f"A massa final do material radioativo será de {massa:.2f} após {tempo} segundos")