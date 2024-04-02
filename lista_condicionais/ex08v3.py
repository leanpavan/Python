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

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def add_seconds_to_date(date, seconds):
    day, month, year, hour, minute, second = date

    second += seconds
    if second >= 60:
        second %= 60
        minute += 1

    if minute >= 60:
        minute %= 60
        hour += 1

    if hour >= 24:
        hour %= 24
        day += 1

    days_in_month = 31
    if month == 2:
        if is_leap_year(year):
            days_in_month = 29
        else:
            days_in_month = 28
    elif month in [4, 6, 9, 11]:
        days_in_month = 30

    if day > days_in_month:
        day = 1
        month += 1

    if month > 12:
        month = 1
        year += 1

    return (day, month, year, hour, minute, second)

def main():
    day = int(input("Dia: "))
    month = int(input("Mês: "))
    year = int(input("Ano: "))
    hour = int(input("Hora: "))
    minute = int(input("Minuto: "))
    second = int(input("Segundo: "))

    date = (day, month, year, hour, minute, second)

    print("Data e hora informadas:", "/".join(map(str, date[:3])), " ", ":".join(map(str, date[3:])))

    add_amount = int(input("Quantidade de segundos a acrescentar: "))
    new_date = add_seconds_to_date(date, add_amount)

    print("Nova data e hora:", "/".join(map(str, new_date[:3])), " ", ":".join(map(str, new_date[3:])))

if __name__ == "__main__":
    main()
