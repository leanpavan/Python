# Turma B 
# Integrante - 1: <Leandro José da Silva Pavan>


A = [
    [3,4,-2],
    [8,0,2],
    [1,1,-2]
]

B = [
    [4,2],
    [4,2],
    [-4,-2]
]

C = [
    [0,2,0],
    [-3,-4,2],
    [7,2,-1]
]


def matrizes(case):
    matriz_aux = []
    # Exercicio V
    if case == "V":
        for i in range(len(A[0])):
            matriz_aux.append([])
            for c in range(len(A[0])):
                matriz_aux[i].append(A[i][c] + C[i][c])
        return matriz_aux
    # Exercicio VI
    elif case == "VI":
        for i in range(3):
            matriz_aux.append([])
            for c in range(2):
                matriz_aux[i].append(B[i][c] - B[i][c])
        return matriz_aux
    # Exercicio VII
    elif case == "VII":
        for i in range(len(A[0])):
            matriz_aux.append([])
            for c in range(len(A[0])):
                matriz_aux[i].append((3 * A[i][c]) - (2 * C[i][c]))
        return matriz_aux


while True:
    try:
        print(f"=== Escolha o exercício que deseja resolver ===\n")
        ex = input("Escolha entre V, VI e VII (0 - Fechar): ")
        if ex == "0":
            break
        else:
            matriz_nova = matrizes(ex)
            for c in matriz_nova:
                print(c)
            print()
    except:
        print(f"Voce digitou o exercício errado!\n")