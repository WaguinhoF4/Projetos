salario = float(input("Digite seu Salario atual: "))

if salario >= 1250:
    salario = salario + (salario * 0.10)
else:
    salario = salario + (salario * 0.15)
print(f"Salario Ajustado R${salario:.2f}")
