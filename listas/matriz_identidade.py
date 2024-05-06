tam = int(input("Digite o tamanho da matriz: "))
aux = tam - 1
matriz = [0] * tam
for i in range(tam):
    matriz[i] = [0] * tam
for c in range(tam):
    for j in range(tam):
        if j == aux:
            matriz[c][j] = 1
    aux -= 1
print(*matriz, sep='\n')
