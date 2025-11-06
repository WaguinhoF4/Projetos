# strip() remove os espaços no inicio e no fim do texto digitado muito util quando alguem
# digita espaço sem querer. startswicth() verifica se a string começa com uma determinada
# palavra ou sequencia de caracteres.

cidade = input("Digte o Nome da Cidade: ").strip().upper()
print(cidade.startswith("SANTO"))
