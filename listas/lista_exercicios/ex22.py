'''Sua organização acaba de contratar um estagiário para trabalhar no Suporte de Informática, com a intenção de
fazer um levantamento nas sucatas encontradas nesta área. A primeira tarefa dele é testar todos os cerca de 200
mouses que se encontram lá, testando e anotando o estado de cada um deles, para verificar o que se pode
aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá
receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse
o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação
igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
'''

mouses = 0
problema = ["necessita da esfera","necessita de limpeza","necessita troca do cabo ou conector","necessita troca do cabo ou conector"]
votos = [0] * 4

while True:
    identificacao = int(input("Digite o número de série do mouse (0 - Finalizar): "))
    mouses += 1
    if mouses > 200:
        break
    if identificacao == 0:
        break
    print("Erros")
    print("1- necessita da esfera ")
    print("2- necessita de limpeza ")
    print("3- necessita troca do cabo ou conector")
    print("4- quebrado ou inutilizado")
    erro = int(input("Digite o erro do mouse: "))
    votos[erro - 1] += 1

print(f"Quantidade de mouses: {mouses}\n")
print(f"Situação", " "*40, "Quantidade", " "*40, "Percentual")
for i in range(len(votos)):
    porcentagem = votos[i] / sum(votos) * 100
    print(f"{i+1}- {problema[i]:<50} {votos[i]:<50} {porcentagem:<6.2f}%")