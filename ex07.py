'''
7. Implemente um programa que solicite o dia, mês e ano (com 4 dígitos) de nascimento
de uma pessoa, e pergunte em qual formato deve exibir a data, como segue:
Código de Exibição de Data
• 1 – Data simples. Ex.: 10/08/1990;
• 2 – Data abreviada. Ex.: 10/ago/1990;
• 3 – Data completa. Ex.: 10 de agosto de 1990
'''
import datetime

dia_nascimento, mes_nascimento, ano_nascimento = map(int, input("Digite o dia, o mês e o ano de seu nascimento no formato (dd mm yyyy): ").split())

# Converter mês de int para string
mes_str = datetime.datetime.strptime(str(mes_nascimento), "%m")
mes_nome = mes_str.strftime("%b")
mes_completo = mes_str.strftime("%B")

formato = input("Em qual formato deseja exibir a data? Simples, Abreviada ou Completa: ")

if formato.lower() == "simples":
    print(f"{dia_nascimento}/{mes_nascimento}/{ano_nascimento}")
elif formato.lower() == "abreviada":
    print(f"{dia_nascimento}/{mes_nome}/{ano_nascimento}")
else:
    print(f"{dia_nascimento} de {mes_completo} de {ano_nascimento}")