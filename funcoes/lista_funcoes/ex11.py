'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva
uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data
'''

meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
meses_31_dias = ["Janeiro", 'Março', "Maio", "Julho", "Agosto", "Outubro", "Dezembro"]


def ano_bissexto(ano):
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        return True
    else:
        return False

def conversor_data(data:str):

    dia, mes, ano = '', '', ''
    estado = 'dia'
    for i in data:
        if estado == 'dia':
            if i != '/':
                dia += i
            else:
                estado = 'mes'
        elif estado == 'mes':
            if i != '/':
                mes += i
            else:
                estado = 'ano'
        else:
            if i != '/':
                ano += i
            else: estado = 'ano'
    return dia, mes, ano


def analisador(dia,mes,ano):
    if int(dia) > 31:
        print("Esse dia não existe")
        return
    elif int(dia) > 30:
        if meses[int(mes)-1] not in meses_31_dias:
            print(f"No mês de {meses[int(mes)-1]} mês não há 31 dias")
            return
    if int(mes) == 2 and int(dia) > 28:
        if not ano_bissexto(int(ano)):
            print("Esse ano não é bissexto")
            return
    print(f"{dia} de {meses[int(mes)-1]} de {ano}")


while True:
    data = input("Digite uma data no formato DD/MM/AAAA (-1 - Finalizar): ")
    if data == '-1':
        break
    else:
        dia, mes, ano = conversor_data(data)
    analisador(dia, mes, ano)
