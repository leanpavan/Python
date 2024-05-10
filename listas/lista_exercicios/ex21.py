'''
Faça um programa que carregue uma lista com os modelos de cinco carros (exemplo de modelos: FUSCA, GOL,
VECTRA etc). Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros cada um desses
carros faz com um litro de combustível. Calcule e mostre:
a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de
1000 quilômetros e quanto isto custará, considerando um que a gasolina custe R$ 2,25 o litro. Abaixo segue
uma tela de exemplo. O disposição das informações deve ser o mais próxima possível ao exemplo. Os
dados são fictícios e podem mudar a cada execução do programa.
'''

modelos = ["fusca", "gol", "uno", "kwid", "peugeot"]
consumo = [7, 10, 12.5, 15.3, 14.5]

economico = consumo.index(min(consumo))
preco_litro = 2.25

print(f"Comparativo de Consumo de Combustível\n")

for i in range(len(modelos)):
    print(f"Veículo {i+1}")
    print(f"Nome: {modelos[i]}")
    print(f"Km por litro: {consumo[i]}\n")

print("Relatório Final")
for j in range(len(modelos)):
    print(f"{j+1} - {modelos[j]} - {consumo[j]} - {1000 / consumo[j]:.1f} litros - R$ {(1000 / consumo[j]) * preco_litro:.2f} ")
print(f"O menor consumo é do {modelos[economico]}")