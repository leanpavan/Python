'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de dados, obtendo
um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um "natural" e ganhou. Se você tirar 2, 3
ou 12 na primeira jogada, isto é chamado de "craps" e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6,
8, 9 ou 10,este é seu "Ponto". Seu objetivo agora é continuar jogando os dados até tirar este número novamente.
Você perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente
'''
import random


def rollDice():
    return random.randint(2, 12)

def craps(natural, deucraps, ponto):
    dice = rollDice()
    if dice in natural:
        print(f"Você GANHOU!!! Seu dado foi {dice}")
        return
    elif dice in deucraps:
        print(f"Você PERDEU :( Seu dado foi {dice}")
        return
    else:
        print(f"Seu ponto é {dice}")
        input("\nPressione ENTER para jogar\n")
        while True:
            aux = rollDice()
            print(f"O dado caiu no {aux}")
            if aux == dice:
                print("Você venceu!!")
                return
            elif aux == 7:
                print("Você perdeu :(")
                return
            else:
                continue


natural = (7, 11)
deucraps = (2, 3, 12)
ponto = (4, 5, 6, 8, 9, 10)
print("Bem vindo ao jogo de CRAPS!!")
print("=" * 30)
while True:
    input("\nPressione ENTER para jogar\n")
    craps(natural, deucraps, ponto)


