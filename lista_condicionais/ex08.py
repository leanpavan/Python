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

def ano_bissexto(ano):
    if ano % 4 != 0:
        return False
    elif ano % 100 != 0:
        return True
    elif ano % 400 != 0:
        return False
    else:
        return True

def adicionar_data(dia, mes, ano, hora, minuto, segundo, add_data, data_type):
    total_segundos = segundo + 60 * (minuto + 60 * hora)
    dias_maximos = [31, ano_bissexto(ano), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if data_type.lower() == "dia":
        total_segundos += dia * 24 * 60 * 60
        dia = 1
    elif data_type.lower() == "hora":
        total_segundos += dia * 24 * 60 * 60 + hora * 60 * 60


# Input
print("Digite a data e hora:")
dia = int(input("Dia: "))
mes = int(input("Mês no formato (1 - Janeiro 2 - Fevereiro, etc): "))
ano = int(input("Ano: "))
hora = int(input("Hora: "))
minuto = int(input("Minuto: "))
segundo = int(input("Segundo: "))

# Input do que vai ser adicionado
data_type = input("Forneça o tipo de informação a ser adicionada (dia, hora, minuto ou segundo): ")
add_data = int(input("Forneça o quanto será adicionado: "))

