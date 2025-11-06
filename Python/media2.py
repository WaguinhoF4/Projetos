print("\033[1;35;46mMEDIA")
n1 = int(input("Digite sua primeira nota: "))
n2 = int(input("Digite sua segunda nota: "))

media = (n1 + n2) / 2
print(f"Sua media é {media}")

if media < 5.0:
    print("Reprovado")
elif 5.0 <= media <= 6.9:
    print("Recuperação")
else:
    print("Aprovado")
