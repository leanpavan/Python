'''Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada
de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados,
faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;'''

notas = []
notas_media = []
abaixo_sete = []

while True:
    nota = int(input("Digite uma  (DIGITE -1 PARA PARAR): "))
    if nota == -1:
        break
    else:
        notas.append(nota)

avg = (sum(notas) / len(notas))
for i in notas:
    if i >= avg:
        notas_media.append(i)
    if i < 7:
        abaixo_sete.append(i)
print(f"A quantidade de valores lidos: {len(notas)}") #a
print(f"Valores: {notas}") #b
print("Valores na ordem inversa:")
for n in reversed(notas): #c
    print(n)

print(f"Soma total das notas: {sum(notas)}") #d
print(f"Média: {avg:.2f}") #e
print(f"Notas acima da média: {notas_media}") #f
print(f"Notas abaixo de 7: {abaixo_sete}") #g
print(f"\nFim do cálculo de notas")