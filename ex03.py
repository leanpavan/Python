'''Criar um jogo de par ou ímpar, onde dois jogadores entram com seu palpite (par ou
ímpar) e seus valores de 1 a 5. Tomar por base os nomes: Jogador 1 e Jogador 2. Caso
um dos valores esteja fora dos parâmetros informados, mostrar uma mensagem
informando que esta rodada não valeu. Caso contrário, informa qual jogador ganhou esta
rodada.'''
import random


regra = random.randint(1,5) % 2

jogador1 = int(input("Jogador 1 - Digite um número de 1 - 5: "))
jogador2 = int(input("Jogador 2 - Digite um número de 1 - 5: "))
soma = (jogador1 + jogador2)

if soma > 10 or soma < 2:
    print("Números escolhidos diferente de 1 - 5, rodada invalidada")
else:
    if regra != 0:  # A regra é ímpar
        if jogador1 % 2 != 0:
            print(f"A regra escolhida foi ímpar e o Jogador 1 venceu!")
        elif jogador2 % 2 != 0:
            print(f"A regra escolhida foi ímpar e o Jogador 2 venceu!")
    else:  # A regra é par
        if jogador1 % 2 == 0:
            print(f"A regra escolhida foi par e o Jogador 1 venceu!")
        else:
            print(f"A regra escolhida foi par e o Jogador 2 venceu!")