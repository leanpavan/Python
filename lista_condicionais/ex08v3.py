from datetime import datetime, timedelta


# Solicita a data e hora ao usuário
dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês: "))
ano = int(input("Digite o ano: "))
hora = int(input("Digite a hora: "))
minuto = int(input("Digite os minutos: "))
segundo = int(input("Digite os segundos: "))

# Cria um objeto datetime com a data e hora fornecidas pelo usuário
date_time = datetime(ano, mes, dia, hora, minuto, segundo)

# Pergunta ao usuário que informação deseja acrescentar e em qual quantidade
unidade = input("Que unidade deseja adicionar (segundo, minuto, hora, dia)? ").lower()
incremento = int(input("Quantidade a ser acrescentada: "))

# Adiciona a quantidade especificada à data e hora
if unidade == "segundo":
    date_time += timedelta(seconds=incremento)
elif unidade == "minuto":
    date_time += timedelta(minutes=incremento)
elif unidade == "hora":
    date_time += timedelta(hours=incremento)
elif unidade == "dia":
    date_time += timedelta(days=incremento)

# Exibe a nova data e hora
print("A nova data é:", date_time.strftime("%d/%m/%Y %H:%M:%S"))