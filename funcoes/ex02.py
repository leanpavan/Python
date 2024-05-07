def string_inverse(text):
    inv = ''
    for l in text:
        inv = l + inv
    return inv

text = input("Digite um texto para inverter: ")
text_inv = string_inverse(text)
print(f"O inverso de {text} é {text_inv}")
