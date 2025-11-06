km_distancia = int(input("Digite a distancia da Viagem em Km: "))

if km_distancia <= 200:
    valor_km = 0.50
    print("O valor do Km será R$0,50")
else:
    valor_km = 0.45
    print("O valor do Km será R$0,45")

preco_passagem = valor_km * km_distancia
print(f"O valor final é R${preco_passagem:.2f}")
