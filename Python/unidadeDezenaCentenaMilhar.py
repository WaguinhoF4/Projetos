num = int(input("Digite um Numero de 0 a 9999: "))
unidade = (num % 10)
dezena = (num // 10) % 10
centena = (num // 100) % 10
milhar = (num // 1000) % 10

print("Unidade:", unidade)
print("Dezena:", dezena)
print("Centena:", centena)
print("Milhar:", milhar)
