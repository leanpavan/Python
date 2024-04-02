'''
3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
'''

objetivo = int(input("Digite a quantidade de pontos necessários para vencer o jogo: "))
pontos = 0

pontosj1 = 0
pontosj2 = 0

while pontos < objetivo:
    jogador1 = int(input("Jogador 1 faça sua jogada (1 - Pedra/2 - Papel/3 - Tesoura): "))
    jogador2 = int(input("Jogador 2 faça sua jogada (1 - Pedra/2 - Papel/3 - Tesoura): "))
    if jogador1 == 1:
        if jogador2 == 2:
            print("Jogador 2 venceu a rodada")
            pontos += 1
            pontosj2 += 1
        if jogador2 == 3:
            print("Jogador 1 venceu a rodada")
            pontos += 1
            pontosj1 += 1
    if jogador1 == 2:
        if jogador2 == 1:
            print("Jogador 1 venceu a rodada")
            pontos += 1
            pontosj1 += 1
        if jogador2 == 3:
            print("Jogador 2 venceu a rodada")
            pontos += 1
            pontosj2 += 1
    if jogador1 == 3:
        if jogador2 == 1:
            print("Jogador 2 venceu a rodada")
            pontos += 1
            pontosj2 += 1
        if jogador2 == 2:
            print("Jogador 1 venceu a rodada")
            pontos += 1
            pontosj1 += 1
    if jogador1 == jogador2:
        print("Empate")

if pontosj1 > pontosj2:
    print(f"\nO jogador 1 venceu")
else:
    print(f"\nO jogador 2 venceu")