# Turma B 
# Integrante - 1: <Lucas Aioria Serpa>
# Integrante - 2: <Guilherme Arcanjo de Morais>
# Integrante - 3: <Rafael Della Giustina> 

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

def calculador_de_matrizes(caso):
    matriz_auxilar = []
    ##Caso 1 == exercicio V
    if caso == 1:
        for c in range(len(A[0])):
            matriz_auxilar.append([])
            for i in range(len(A[0])):
                matriz_auxilar[c].append(A[c][i] + C[c][i])
        return matriz_auxilar
    #Caso 2 == exercicio VI
    elif caso == 2:
        for c in range(3):
            matriz_auxilar.append([])
            for i in range(2):
                matriz_auxilar[c].append(B[c][i] - B[c][i])
        return matriz_auxilar
    #Caso 3 == exercicio VII
    elif caso == 3:
        for c in range(len(A[0])):
            matriz_auxilar.append([])
            for i in range(len(A[0])):
                matriz_auxilar[c].append((3 * A[c][i]) - (2 * C[c][i]))
        return matriz_auxilar

while True:
    try:
        print(f"*** Escolha um dos exercicios ***")
        print("Digite 0 Para fechar...")
        aux = int(input("Escolha entre 1 2 ou 3: "))
        if aux == 0: break
        else:
            matriz_nova = calculador_de_matrizes(aux)
            for c in matriz_nova:
                print(c)
            print()
    except aux > 3 or aux < 0:
        print("Voce digitou um numero errado!")
        print("digite 1 para o ex V, 2 para o ex VI e 3 para o ex VII")
        print()
    except ValueError:
        print("O parametro deve ser um numero!")
        print()