'''
Como navegador de uma nave interestelar da frota Alfa, uma de suas principais funções
á calcular as distâncias no espaço. Para isto, realizar rapidamente conversão de unidades
de tempo é uma habilidade fundamental em seu trabalho. Assim sendo, a fim de facilitar
seu próprio trabalho, você, programador em linguagem Python, decide desenvol ver seu
próprio conversor unidades de tempo em deslocamento no espaço. Para tanto,
consegue as seguintes informações de base para seu programa: um dicionário chamado
anos_luz, que tem os valores das demais unidades de tempo convertidos para valor em
anos luz, e uma lista chamada unidades com o nome e abreviações das unidades de
tempo, como segue:
ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz
(ml)", "Segundo-Luz (sl)"]
Desta forma, sua tarefa é desenvolver um programa com as seguintes funcionalidades:
- Imprimir a lista de unidades de conversão
- Solicitar o valor que se deseja converter usando a frase “Valor a ser convertido: ”
- Solicitar a unidade origem do valor usando a frase “Converter de: ”
- Solicitar a unidade destino de conversão usando a franse “Converter para: ”
- Exibir o valor convertido com a frase “Conversão: {valor} {unidade origem} = {valor}
{unidade destino}”
A frota Alfa conta com você, oficial navegador!!!
'''

ano_luz = {
"pc": 0.31,
"al": 1,
"ae": 63241.09,
"ml": 525960.23,
"sl": 31557609.92
}

unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz(ml)", "Segundo-Luz (sl)"]

for u in unidades:
    print(u)

valor = int(input(f"\nValor a ser convertido: "))
unidade_origem = input("Converter de: ")
unidade_destino = input("Converter para: ")

if unidade_origem not in ano_luz or unidade_destino not in ano_luz:
    print("Unidades de conversão inválidas")
else:
    valor_convertido = valor * ano_luz[unidade_origem] / ano_luz[unidade_destino]
    print(f"Conversão: {valor} {unidade_origem} = {valor_convertido}{unidade_destino}")