print("-=-" * 20)
print("\033[4;34;43mEMPRÉSTIMO BANCÁRIO\033[m")
print("-=-" * 20)

casa = float(input("Digite o valor da casa: R$ "))
salario = float(input("Digite seu salário: R$ "))
anos = int(input("Quantos anos você pretende pagar o empréstimo: "))

prestacao_mensal = casa / (anos * 12)
minimo = salario * 30 / 100

print(f"\nPara pagar uma casa de R$ {casa:.2f} em {anos} anos, "
      f"a prestação será de R$ {prestacao_mensal:.2f}")

if prestacao_mensal <= minimo:
    print("\033[1;30;42mEMPRÉSTIMO APROVADO\033[m")
else:
    print("\033[1;33;41mEMPRÉSTIMO NEGADO\033[m")
