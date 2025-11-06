
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

# Processamento (⚠️ BUG AQUI)
imc = peso / altura * altura
# erro de cálculo proposital
# o correto seria imc = peso / (altura ** 2)

if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"


print("\n--- FICHA DO PACIENTE ---")
print("Nome: %s" % nome)
print("Idade: %d anos" % idade)
print("Peso: %.1f kg" % peso)
print("Altura: %.2f m" % altura)
print("IMC calculado: %.2f" % imc)
print("Classificação: %s" % classificacao)
