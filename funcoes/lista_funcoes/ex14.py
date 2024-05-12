'''
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, com um número em cada
posição e no qual a soma das linhas, colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de
lado 3, com números de 1 a 9:
'''
import random

def quadrado_magico():
    while True:
        matriz = [[],[],[]]
        historico = []
        for i in range(3):
            for j in range(3):
                while True:
                    n = random.randint(1, 9)
                    if n not in historico:
                        matriz[i].append(n)
                        historico.append(n)
                        break
        aux = sum(matriz[0])
        if all(sum(linha) == aux for linha in matriz) and \
           all(sum(matriz[i][j] for i in range(3)) == aux for j in range(3)) and \
           sum(matriz[i][i] for i in range(3)) == aux and \
           sum(matriz[i][2-i] for i in range(3)) == aux:
            return matriz

while True:
    input("Aperte ENTER para gerar um quadrado mágico")
    qmagic = quadrado_magico()
    for c in qmagic:
        print(c)
