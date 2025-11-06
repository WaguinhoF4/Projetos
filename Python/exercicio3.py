nome: str
idade: int
altura: float


nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print("Nome: %s" % nome)
print("Idade: %d" % idade)
print("Altura: %.2f" % altura)
