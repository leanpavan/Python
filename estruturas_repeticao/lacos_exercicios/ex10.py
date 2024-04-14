'''
10. Solicitar ao usuário duas datas e calcular a quantidade de dias entre elas (levar em
consideração os anos bissextos)
'''

dia, mes,ano,dia2,mes2,ano2 = '', '', '', '', '', ''
p_data = input("Digite uma data: ")
s_data = input("Digite a segunda data: ")
estado = 'dia'
estado1 = 'dia'
numeros = set("0123456789")

#Parsing da primeira data
for i in p_data:
    if estado == 'dia':
        if i in numeros:
            dia += i
        elif dia:
            estado = "mes"
    elif estado == "mes":
        if i in numeros:
            mes += i
        elif mes:
            estado = "ano"
    elif estado == "ano":
        if i in numeros:
            ano += i

#Parsing da segunda data
for i in s_data:
    if estado1 == 'dia':
        if i in numeros:
            dia2 += i
        elif dia:
            estado1 = "mes"
    elif estado1 == "mes":
        if i in numeros:
            mes2 += i
        elif mes:
            estado1 = "ano"
    elif estado1 == "ano":
        if i in numeros:
            ano2 += i

dia = int(dia)
mes = int(mes)
ano = int(ano)
dia2 = int(dia2)
mes2 = int(mes2)
ano2 = int(ano2)

#Validação do ano bissexto
if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            bissexto = True
        else:
            bissexto = False
    else:
        bissexto = False
else:
    bissexto = False

if ano2 % 4 == 0:
    if ano2 % 100 == 0:
        if ano2 % 400 == 0:
            bissexto2 = True
        else:
            bissexto2 = False
    else:
        bissexto2 = False
else:
    bissexto2 = False

#Transformar os meses em dias
for x in range(mes):
    if x >= 1:
            dia += 31
    if x >= 2:
        if bissexto == True:
            dia += 29
        else:
            dia += 28
    if x >= 3:
            dia += 31
    if x >= 4:
            dia += 30
    if x >= 5:
            dia += 31
    if x >= 6:
            dia += 30
    if x >= 7:
            dia += 31
    if x >= 8:
            dia += 31
    if x >= 9:
            dia += 30
    if x >= 10:
            dia += 31
    if x >= 11:
            dia += 30
    if x >= 12:
            dia += 31

for x in range(mes2):
    if x >= 1:
            dia2+= 31
    if x >= 2:
        if bissexto2 == True:
            dia2 += 29
        else:
            dia2 += 28
    if x >= 3:
            dia2 += 31
    if x >= 4:
            dia2 += 30
    if x >= 5:
            dia2 += 31
    if x >= 6:
            dia2 += 30
    if x >= 7:
            dia2 += 31
    if x >= 8:
            dia2 += 31
    if x >= 9:
            dia2 += 30
    if x >= 10:
            dia2 += 31
    if x >= 11:
            dia2 += 30
    if x >= 12:
            dia2 += 31

#Transformar os anos em dias
for y in range(400, ano+1):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                dia += 366
            else:
                dia += 366
        else:
            dia += 366
    else:
        dia += 366

for y in range(400, ano2+1):
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                dia2 += 366
            else:
                dia2 += 366
        else:
            dia2 += 366
    else:
        dia2 += 366

#Cálculo final
soma = dia - dia2
if soma < 0:
    soma *= -1

print(f"A quantidade de dias que passou entre essas duas datas foi {soma}")