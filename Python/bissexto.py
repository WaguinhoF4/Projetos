from datetime import date  # Modulo de Datas
ano = int(input("Digite o Ano: "))
if ano == 0:
    ano = date.today().year  # Se vc digitar 0 ele pega a data do ano configurado na maquina
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é BISSEXTO")
else:
    print(f"O ano de {ano} não é BISSEXTO")
