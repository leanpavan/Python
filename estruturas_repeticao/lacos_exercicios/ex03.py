'''
3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
'''

objetivo = int(input("Digite a quantidade de pontos necessários para vencer o jogo: "))
pontos = 0

pontosj1 = 0
pontosj2 = 0

while pontosj1 < objetivo or pontosj2 < objetivo:
    jogador1 = input("Jogador 1 faça sua jogada (Pedra/Papel/Tesoura): ")
    jogador2 = input("Jogador 2 faça sua jogada (Pedra/Papel/Tesoura): ")
    if jogador1 != jogador2:
        if jogador1.lower() == "pedra": #Jogador 1 jogou pedra
            if jogador2.lower() == "tesoura":
                pontosj1 +=1
                pontos += 1
                print("Jogador 1 Venceu a rodada")
            elif jogador2.lower() == "papel":
                pontosj2 +=1
                pontos += 1
                print("Jogador 2 Venceu a rodada")
        elif jogador1.lower() == "papel": #Jogador 1 jogou papel
            if jogador2.lower() == "tesoura":
                pontosj2 +=1
                pontos += 1
                print("Jogador 2 Venceu a rodada")
            elif jogador2.lower() == "pedra":
                pontosj1 +=1
                pontos += 1
                print("Jogador 1 Venceu a rodada")
        elif jogador1.lower() == "tesoura": #Jogador 1 jogou tesoura
            if jogador2.lower() == "pedra":
                pontosj2 +=1
                pontos += 1
                print("Jogador 2 Venceu a rodada")
            elif jogador2.lower() == "papel":
                pontosj1 +=1
                pontos += 1
                print("Jogador 1 Venceu a rodada")
    else:
        print("Empate")

if pontosj1 > pontosj2:
    print("O jogador 1 venceu")
else:
    print("O jogador 2 venceu")