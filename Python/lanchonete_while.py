total = 0.0
opcao = ""

print(" Bem-vindo à Lanchonete do WAGNER!")
print("Digite o código do item que deseja pedir:")
print("1 - X-Burguer........... R$ 12.00")
print("2 - X-Salada............ R$ 14.00")
print("3 - Refrigerante........ R$ 5.00")
print("4 - Batata Frita........ R$ 7.00")
print("0 - Finalizar pedido")

while True:
    opcao = input("Digite o código do produto (ou 0 para sair): ")

    if opcao == "1":
        total += 12.00
        print("X-Burguer adicionado!")

    elif opcao == "2":
        total += 14.00
        print("X-Salada adicionado!")

    elif opcao == "3":
        total += 5.00
        print("Refrigerante adicionado!")

    elif opcao == "4":
        total += 7.00
        print("Batata Frita adicionada!")

    elif opcao == "0":
        print(f"Total a pagar: R$ {total}")
        print("Pedido finalizado. Volte sempre!")
        break

    else:
        print("Código inválido. Tente novamente.")
