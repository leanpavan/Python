dimensao = 4
matriz = [
    [9, 1, 2, 4],
    [5, 6, 7, 8],
    [3, 2, 1, 0],
    [1, 2, 3, 4]
]

for i in range(dimensao):
    dest = dimensao - i - 1
    if i < dimensao // 2:
        matriz[i][i], matriz[dest][dest] = matriz[dest][dest], matriz[i][i]
    matriz[i][dest] *= 2

print(*matriz, sep='\n')