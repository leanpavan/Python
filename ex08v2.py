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
from datetime import timedelta

# Checar se o ano é bissexto
def ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def converter_segundos(hora, minuto, segundo):
    segundo_somado = segundo + (minuto * 60) + (hora * 3600)
    return segundo_somado

# Variáveis
dia, mes, ano = map(int, input("Digite uma data no formato dd mm aaaa (Apenas números): ").split())
hora, minuto, segundo = map(int, input("Digite a hora no formato hh mm ss: ").split())
info = input("Digite a informação que deseja adicionar (dia, mês, ano, segundo, minuto ou hora): ").lower()
quantidade = int(input("Digite o valor que deseja adicionar à data: "))



# Condicionais
if info == "dia":
    dia += quantidade
    if mes == 1 or 3 or 5 or 7 or 8 or 10: #Checa se o mês tem 31 dias
        if dia > 31:
            dia -= 31
            mes += 1
    elif mes == 4 or 6 or 9 or 11: #Checa se o mês tem 30 dias
        if dia > 30:
            dia -= 30
            mes += 1
    elif mes == 2: #Checa se é fevereiro
        if ano_bissexto(ano):
            if dia > 29:
                dia -= 29
                mes += 1
        else:
            if dia > 28:
                dia -= 28
                mes += 1
    elif mes == 12:
        if dia > 31:
            dia -= 31
            mes -= 12
            mes += 1
            ano += 1

if info == "mes":
    mes += quantidade
    if mes > 12:
        mes -= 12
        ano += 1

if info == "ano":
    ano += 1

if info == "segundo":
    segundo += quantidade

segundo_somado = converter_segundos(hora, minuto, segundo)
td = timedelta(seconds=segundo_somado)

print('Tempo em segundos:', segundo_somado)
#print('Tempo em hh:mm:ss:', td)

print(f"{dia}/{mes}/{ano} {td}")