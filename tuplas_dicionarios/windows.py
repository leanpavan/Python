os = {"Windows": 0, "Unix": 0, "Linux": 0, "Netware": 0, "Mac OS": 0, "Outro": 0}
sistemas = list(os.keys())

print(f"Qual o melhor Sistema Operacional para uso em servidores?\n")
print(f"As possíveis respostas são:\n")
for i in range(len(os)):
    print(f"{i+1}- {sistemas[i]}")

while True:
    try:
        voto = (input("\nQual o melhor Sistema Operacional (0 - Finalizar): "))
        if voto == "0":
            break
        if voto not in os:
            raise ValueError
        os[voto] += 1
        for values in os.values():
            print(values)
    except ValueError:
        print("\nSistema Operacional inválido! Digite Novamente")
        continue