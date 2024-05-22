def criar_matriz(tamanho):
    matriz = []
    for i in range(tamanho):
        matriz.append([])
        for _ in range(tamanho):
            matriz[i].append(0)
    for i in range(tamanho):
        for c in range(tamanho):
            if c == i:
                matriz[i][c] += 1
    for i in matriz:
        print(i)

tamanho = int(input("Qual será o tamanho da matriz?: "))
criar_matriz(tamanho)