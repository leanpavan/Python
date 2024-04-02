'''

8. Implemente um programa que solicite uma data com hora, pedindo em separado: dia,
mês, ano, hora, minuto e segundo. Pergunte ao usuário que informação ele deseja
acrescentar, e em qual quantidade. Informar a nova data de acordo com o solicitado pelo
usuário.
Ex.: Informada a data 31/12/2001 23:59:59, se o usuário pedir para acrescentar um
segundo a data deve ser exibida como 01/01/2002 00:00:00.
Para determinar se um ano é bissexto, execute estas etapas:
1. Se o ano for uniformemente divisível por 4, vá para a etapa 2. Caso contrário, vá
para a etapa 5.
2. Se o ano for uniformemente divisível por 100, vá para a etapa 3. Caso contrário,
vá para a etapa 4.
3. Se o ano for uniformemente divisível por 400, vá para a etapa 4. Caso contrário,
vá para a etapa 5.
4. O ano é bissexto (tem 366 dias).
5. O ano não é um ano bissexto (tem 365 dias)

'''
from datetime import datetime, timedelta

# Solicita a data e hora ao usuário
day = int(input("Digite o dia: "))
month = int(input("Digite o mês: "))
year = int(input("Digite o ano: "))
hour = int(input("Digite a hora: "))
minute = int(input("Digite os minutos: "))
second = int(input("Digite os segundos: "))

# Cria um objeto datetime com a data e hora fornecidas pelo usuário
date_time = datetime(year, month, day, hour, minute, second)

# Pergunta ao usuário que informação deseja acrescentar e em qual quantidade
unit = input("Que unidade deseja adicionar (segundo, minuto, hora, dia)? ").lower()
increment = int(input("Quantidade a ser acrescentada: "))

# Adiciona a quantidade especificada à data e hora
if unit == "segundo":
    date_time += timedelta(seconds=increment)
elif unit == "minuto":
    date_time += timedelta(minutes=increment)
elif unit == "hora":
    date_time += timedelta(hours=increment)
elif unit == "dia":
    date_time += timedelta(days=increment)

# Exibe a nova data e hora
print("A nova data é:", date_time.strftime("%d/%m/%Y %H:%M:%S"))
