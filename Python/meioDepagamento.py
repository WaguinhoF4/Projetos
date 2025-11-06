from time import sleep
print("======Calculadora de Pagamento======")

preco = float(input("Digite o valor do produto "))

print("\nFormas de Pagamentos:")
print("1 - À vista dinheiro/cheque (10% de desconto)")
print("2 - À vista no cartão (5% de desconto)")
print("3 - Em até 2x no cartão (preço normal)")
print("4 - 3x ou mais no cartão (20% de juros)")

opçao = int(input("Escolha a opção (1/2/3/4): "))
sleep(5)

if opçao == 1:
    total = preco - (preco * 0.10)
    print(f"Valor final com 10% de desconto: R${total:.2f}")
elif opçao == 2:
    total = preco - (preco * 0.05)
    print(f"Valor final com 5% de desconto: R${total:.2f}")
elif opçao == 3:
    total = preco
    print(f"Valor final sem desconto: R${total:.2f}")
elif opçao == 4:
    total = preco + (preco * 0.20)
    print(f"Valor final com 20% de desconto: R${total:.2f}")
else:
    print("Opção Invaliada")
