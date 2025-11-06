# split divide o nome completo em palavras separadas por espaços, e armazena numa lista.
# repleace (" ", "") Remove todos os espaços do nome.
# len(partes[0])conta quantas letras tem o primeiro nome.
# upper transforma tudo em maisculo e lower em minuscolo

nome_completo = str(input("Escreva seu Nome: "))
partes = nome_completo.split()
frase = nome_completo
print(partes)
print("Total de Letras sem Espaços: ", len(frase.replace(" ", "")))
print("Numero de Letras No Primeiro Nome:", len(partes[0]))
print("Nome em Maiusculo: ", frase.upper())
print("Nome em Minusculo: ", frase.lower())
