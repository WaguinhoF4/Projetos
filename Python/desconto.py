preço = float(input("Digite o Preço do Produto: R$"))
novo = preço - (preço * 5 / 100)
print(
    f"O produto que custava R${preço}, na Promoção com desconto de 5% vai custar R${novo}")
