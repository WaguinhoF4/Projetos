from datetime import date
ano_atual = date.today().year  # aqui pegamos o ano atual
print("-=-" * 30)
print("\033[1;33;42mALISTAMENTO MILITAR\033[m")
print("-=-" * 30)

ano_nascimento = int(input("Digite seu ano de nascimento: "))

idade = ano_atual - ano_nascimento

print(f"Você tem {idade} anos.")

if idade == 18:
    print("Hora de sé alistar.")
elif idade < 18:
    falta = 18 - idade
    print(f"Vocé ainda vai se alistar. Faltam {falta} ano(s).")
elif idade > 18:
    passou = idade - 18
    print(f"Você já deveria ter se alistado há {passou} anos(s). ")
