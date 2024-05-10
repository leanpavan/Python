'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva
uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data
'''


def date_format(date_input):
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    date,count = [[]],0
    date_str = ""
    day,month,year = '','',''
    for i in date_input:
        if i == '/':
            date.append([])
            count += 1
            continue
        date[count].append(i)
    for c in date:
        for j in c:
            date_str += j
    day_list = date[0]
    month_list = date[1]
    year_list = date[2]
    aux = ""
    for i in day_list:
        day = day + i
    for i in month_list:
        month = month + i
    for i in year_list:
        year = year + i
    print(day,month,year)
    return date_str,day,month,year


date_input = input("Digite uma data no formato DD/MM/AAAA: ")
print(date_format(date_input))