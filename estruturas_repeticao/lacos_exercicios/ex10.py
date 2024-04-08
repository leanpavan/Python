'''
10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos)
'''

day1, month1, year1 = map(int, input("Digite uma data no formato dd mm yyyy: ").split("/"))
day2, month2, year2 = map(int, input("Digite outra data no formato dd mm yyyy: ").split("/"))

b1 = year1 % 4 == 0 and year1 % 400 != 0
dy1 = 365