# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno,
# imprima o número de alunos com média maior ou igual a 7.0.

medias = []
alunos_media = 0

for i in range(10): # Todos os 10 alunos
    for c in range(4): # Para cada aluno individualmente
        aux = []
        aux.append(float(input(f"Digite a nota {c+1} do aluno {i+1}: ")))
    medias.append(sum(aux) / len(aux))

for i in range(10):
    if medias[i] >= 7:
        alunos_media += 1

print(f"O número de alunos com média maior ou igual a 7.0 foi: {alunos_media}")