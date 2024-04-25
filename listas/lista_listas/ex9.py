# Criar um programa que solicite o nome de 4 times de futebol. O
# programa deve simular partidas de forma que cada time jogue
# uma vez com os outros 3 times. Na partida deve perguntar
# quantos gols fez cada time, e somar as devidas pontuações. Ao
# final deve dizer qual ou quais times foram campeões, uma vez
# que pode haver empate em pontuação. Obs.: vitória vale 3
# pontos para o vencedor, empate vale 1 ponto para cada time e
# derrota não soma pontos.

'''
i x j
0 x 1
0 x 2
0 x 3
1 x 2
1 x 3
2 x 3
6 partidas
'''

times = []
pontos = [0, 0, 0, 0]
vencedores = []

for _ in range(4):
    nome_time = input("Forneça o nome do time: ")
    times.append(nome_time)
print(times)
for i in range(3): # varia entre 0 1 e 2
    for j in range(i+1, 4):
        golsa = int(input(f"Digite o número de gols do time {times[i]}: "))
        golsb = int(input(f"Digite o número de gols do time {times[j]}: "))
        if golsa == golsb:
            pontos[i] += 1
            pontos[j] += 1
            print(f"\nOs dois times empataram!")
        elif golsa > golsb:
            pontos[i] += 3
            print(f"\nO time {times[i]} ganhou a partida!")
        elif golsb > golsa:
            pontos[j] += 3
            print(f"\nO time {times[j]} ganhou a partida!")
        # print(times[i], times[j])
        print(pontos)
m_pontos = max(pontos)
m_index = pontos.index(m_pontos)

if pontos.count(m_pontos) == 1:
    print(f"O time vencedor do campeonato foi o {times[m_index]}")
else:
    for i in range(4):
        if pontos[i] == m_pontos:
            vencedores.append(times[i])

    print(f"O campeonato empatou! Os times que empataram foram: {vencedores} ")