'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um grande quantidade de
organizações:
'''

print("Qual o melhor Sistema Operacional para uso em servidores?")
print(f"\nAs possíveis respostas são:")
possiveis_respostas = '''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
'''
print(possiveis_respostas)
votos = []
while True:
    resposta = int(input("Digite sua resposta (Digite 0 para parar): "))
    if resposta == 0:
        break
    elif resposta > 6:
        continue
    else:
        votos.append(resposta)
        print(votos)

windows = votos.count(1) / len(votos) * 100
unix = votos.count(2) / len(votos) * 100
linux = votos.count(3) / len(votos) * 100
netware = votos.count(4) / len(votos) * 100
mac = votos.count(5) / len(votos) * 100
outro = votos.count(6) / len(votos) * 100
print(windows)
