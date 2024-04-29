'''
A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de
arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos
usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele
conseguiu gerar o seguinte arquivo, chamado "usuarios.txt"
'''

''' usuarios.txt
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125
'''

''' relatorio.txt
ACME Inc. Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr. Usuário Espaço utilizado % do uso
1 alexandre 434,99 MB 16,85%
2 anderson 1187,99 MB 46,02%
3 antonio 117,73 MB 4,56%
4 carlos 87,03 MB 3,37%
5 cesar 0,94 MB 0,04%
6 rosemary 752,88 MB 29,16%
Espaço total ocupado: 2581,57 MB
Espaço médio ocupado: 430,26 MB
'''

usuarios = ["Alexandre", "Anderson", "Antonio", "Carlos", "Cesar", "Rosemary"]
bytes = [456123789, 1245698456, 123456456, 91257581, 987458, 789456125]
megabytes = []
used_space = 0
avg_space = 0
use_percentage = []

for i in range(len(bytes)):
    megabytes.append(bytes[i] / 1024**2)

used_space = sum(megabytes)
avg_space = used_space / len(bytes)

for i in range(len(megabytes)):
    use_percentage.append((megabytes[i] / used_space) * 100)

#relatorio.txt
print(f"\nACME Inc. Uso do espaço em disco pelos usuários")
print("------------------------------------------------------------------------")
print("Nr.  Usuário     Espaço utilizado   % do uso")
for i in range(len(usuarios)):
    print(f"{i+1:<5}{usuarios[i]:<13}{megabytes[i]:>12.2f} MB{use_percentage[i]:>9.2f} %")
print(f"\nEspaço total ocupado: {used_space:.2f}")
print(f"Espaço médio ocupado: {avg_space:.2f}")