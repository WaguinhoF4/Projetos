nota: float

nota = float(input("Digite sua Nota: "))

if nota >= 7:
    print("Aprovado")
elif nota >= 5 and nota < 7:
    print("Recuperação")
else:
    print("Reprovado")
