# Foram anotadas as idades e alturas de 30 alunos. Faça um Programa que determine quantos alunos com mais de
# 13 anos possuem altura inferior à média de altura desses alunos.

num_alunos = 30
idades = []
alturas = []
media_altura = 0
count = 0

for i in range(num_alunos):
    idade_aluno = int(input(f"Digite a idade do {i+1}º aluno: "))
    altura_aluno = int(input(f"Digite a altura do {i+1}º aluno em centímetros: "))
    idades.append(idade_aluno)
    alturas.append(altura_aluno)

media_altura = sum(alturas) / len(alturas)

for i in range(num_alunos):
    if idades[i] > 13 and alturas[i] < media_altura:
        count += 1


print(idades)
print(alturas)
print(media_altura)
print(f"O número de alunos com altura menor que a média é {count}")
