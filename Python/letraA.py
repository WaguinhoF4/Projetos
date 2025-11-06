frase = input("Digite uma Frase: ").strip().upper()

quantidade_a = frase.count("A")
posicao_primeiro_a = frase.find("A")
posicao_ultimo_a = frase.rfind("A")

print(quantidade_a)
print(posicao_primeiro_a)
print(posicao_ultimo_a)
print(
    f" A quantidade de {quantidade_a}, a posição do primeiro A é {posicao_primeiro_a},", end='')
print(f" é o ultimo A fica na posção {posicao_ultimo_a}")
