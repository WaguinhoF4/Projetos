x: int
soma: int

N = int(input("Quantos numeros serão Digitados: "))

soma = 0
for i in range(0, N):
    x = int(input("Digite um Numero"))
    soma = soma + x

print("SOMA = ", soma)
