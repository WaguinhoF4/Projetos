print("=" * 20)
print("\033[1;31;47mCONVERSOR DE NUMEROS\033[m")
print("=" * 20)

n = int(input("Digite um Numero: "))

print("Escolha a base para conversão:")
print("1 - Binário")
print("2 - Octal")
print("3 - Hexadecimal")
print("4 - Cancelar Operação")

opcao = int(input("Opção: "))

if opcao == 1:
    print(f"BINÁRIO: {bin(n)[2:]}")
elif opcao == 2:
    print(f"OCTAL: {oct(n)[2:]}")
elif opcao == 3:
    print(f"HEXADECIMAL: {hex(n)[2:]}")
else:
    print("\033[1;31;47mOPERAÇÃO CANCELADA\033[m")
