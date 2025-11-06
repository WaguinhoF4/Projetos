print("Calculadora de IMC")

peso = float(input("Digite seu peso em Kg: "))
altura = float(input("Digite sua altura em Metros: "))

calculo_IMC = peso / (altura ** 2)

if calculo_IMC <= 18.5:
    print("Abaixo do peso")
elif 18.5 < calculo_IMC <= 25:
    print("Peso normal")
elif 25 < calculo_IMC <= 30:
    print("Sobrepeso")
elif 30 < calculo_IMC <= 40:
    print("Obesidade")
else:
    print("Obesidade mórbida")

print(f"Seu IMC e de {calculo_IMC:.1f}")
