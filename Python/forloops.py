total_idade = 0
for pessoa in range(1, 5):
    nome = str(input("Digite seu Nome:"))
    idade = int(input("Digte sua idade:"))
    total_idade += idade
    media = total_idade / 4
print(f"A média de idade do grupo é {media:.2f} ")
