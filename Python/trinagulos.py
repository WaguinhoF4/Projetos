r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas PODEM formar um triângulo. ", end="")
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")
else:
    print("As retas NÃO PODEM formar um triângulo.")
