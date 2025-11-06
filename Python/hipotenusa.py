# A Dois metodos de Fazer isso um com Hypot é outro com sqrt, Com sqrt ficaria assim.
# from math import sqrt
# cateto_oposto = float(input("Digite o Tamanho do Cateto Oposto: "))
# cateto_adjacento = float(input("Digite o Tamnho do Cateto Adjecento: "))
# hipotenusa = sqrt(cateto_adjacento ** 2 + cateto_oposto **2)
# print(f"O valor da Hipotenusa é {hipotenusa:.2f}")
# A diferença do sqrt para Hypot e que o sqrt tira a raiz quadrada de um numero, voce precisa
# fazer o passo a passo. Já o Hypot faz tudo isso, mais de forma mais elegante sem precisar
# de passo a passo e tudo interno.

from math import hypot

cateto_oposto = float(input("Digite o Tamanho do Cateto Oposto: "))
cateto_adjacento = float(input("Digite o Tamnho do Cateto Adjecento: "))

hipotenusa = hypot(cateto_adjacento, cateto_oposto)
print(f"O valor da Hipotenusa é {hipotenusa:.2f}")
