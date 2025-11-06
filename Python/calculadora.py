a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
operação = input("Escolha a operação (+, -, *, /): ")

if operação == "+":
    print("Resultado", a + b)
elif operação == "-":
    print("Resultado", a - b)
elif operação == "*":
    print("Resultado", a * b)
elif operação == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Divisão por zero!")
else:
    print("Operação inválida.")
