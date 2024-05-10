'''
Uma grande emissora de televisão quer fazer uma enquete entre os seus telespectadores para saber qual o melhor
jogador após cada jogo. Para isto, faz-se necessário o desenvolvimento de um programa, que será utilizado pelas
telefonistas, para a computação dos votos. Sua equipe foi contratada para desenvolver este programa, utilizando a
linguagem de programação C++. Para computar cada voto, a telefonista digitará um número, entre 1 e 23,
correspondente ao número da camisa do jogador. Um número de jogador igual zero, indica que a votação foi
encerrada. Se um número inválido for digitado, o programa deve ignorá-lo, mostrando uma breve mensagem de
aviso, e voltando a pedir outro número. Após o final da votação, o programa deverá exibir:
'''

votos_computados = 0
jogadores = [0] * 23

print(f"Enquete: Quem foi o melhor jogador?\n")

while True:
    try:
        jogador = int(input("Número do jogador (0=fim): "))
        if jogador == 0:
            break
        if not (0 <= jogador <= 23):
            raise ValueError
        votos_computados += 1
        jogadores[jogador-1] += 1
    except ValueError:
        print("Jogador inválido")
        continue

print(jogadores)
jogador_recorrente = jogadores.index(max(jogadores)) + 1
votos_recorrente = max(jogadores)
print(jogador_recorrente)

print(f"Resultado da votação:\n")

print(f"Foram computados {votos_computados} votos.\n")

print(f"Jogador      Votos          %\n")
for i in range (0,23):
    porcentagem = jogadores[i] / len(jogadores)
    print(f"{i+1:<17}{jogadores[i]:}{porcentagem*100:>10.2f}%")

print(f"\nO melhor jogador foi o número {jogador_recorrente}, com {votos_recorrente} votos, correspondendo a {votos_recorrente / sum(jogadores) * 100:.2f}% do total de votos.")