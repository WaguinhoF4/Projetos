
nome = input("Digite o nome do funcionário(a): ")
valor_hora = float(input("Digite o valor por hora: "))
horas_trabalhadas = int(input("Digite as horas trabalhadas: "))


pagamento = valor_hora * horas_trabalhadas

print("O pagamento para", nome, "deve ser R$", round(pagamento, 2))
