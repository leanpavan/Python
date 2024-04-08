'''
3. Criar um jogo de pedra, papel, tesoura entre dois jogadores. Antes de começar o jogo,
porém, deve ser escolhido a quantidade de pontos a serem feitos para vencer.
'''

pontos = int(input("Digite a pontuação necessária para a vitória: "))
pontuacao_player1, pontuacao_player2 = 0, 0
while pontuacao_player1 < pontos and pontuacao_player2 < pontos:
    jogada1 = int(input("Player 1: Qual será sua jogada? [1 - PEDRA, 2 - PAPEL, 3 - TESOURA]: "))
    jogada2 = int(input("Player 2: Qual será sua jogada? [1 - PEDRA, 2 - PAPEL, 3 - TESOURA]: "))
    if jogada1 == 1 and jogada2 == 3 or jogada1 == 2 and jogada2 == 1 or jogada1 == 3 and jogada2 == 2:
        pontuacao_player1 += 1
        print("Player 1 vence a rodada!")
        print(f"Player1: {pontuacao_player1} Player 2: {pontuacao_player2}")
    else:
        pontuacao_player2 += 1
        print("Player 2 vence a rodada!")
        print(f"Player1: {pontuacao_player1} Player 2: {pontuacao_player2}")

if pontos == pontuacao_player1:
    print("Vitória do Player 1")
else:
    print("Vitória do Player 2")