
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))
peso = float(input("Digite seu peso em kg: "))


imc = peso / (altura ** 2)

print("\n--- FICHA CADASTRAL ---")
print("Nome: %s" % nome)
print("Idade: %d anos" % idade)
print("Altura: %.2f m" % altura)
print("Peso: %.1f kg" % peso)
print("IMC calculado: %.2f" % imc)
