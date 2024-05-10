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
votos = [0] * 6
while True:
    try:
        resposta = int(input("Digite sua resposta (Digite 0 para parar): "))
        if resposta == 0:
            break
        if not (0 <= resposta <= 6):
            raise ValueError
        votos[resposta-1] += 1
        print(votos)
    except ValueError:
        print("Voto invalido")
        continue
os = ["Windows Server", "Unix", "Linux", "Netware", "Mac OS", "Outro"]
total_votos = sum(votos)


print(f"\nSistema Operacional       Votos       %")
print(f"-------------------       -----       ---")
for i in range(len(votos)):
    porcentagem = votos[i] / total_votos * 100
    print(f"{i+1}- {os[i]:<27}{votos[i]:}{porcentagem:>9.2f}%")
print(f"-------------------       -----")
print(f"Total{total_votos:>27}")