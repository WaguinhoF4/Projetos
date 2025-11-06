import random
from time import sleep  # faz o computador dormir por alguns segundos
numero_computador = random.randint(0, 5)  # faz o computador pensar.
# jogador tenta adivinhar
palpite = int(input("\033[0;30;44mTente adivinha o Numero 0 a 5: \033[m"))
print("\033[7;35;47mPROCESSANDO...\033[m")
sleep(5)  # 5 segundos

if palpite == numero_computador:
    print("-=-" * 20)
    print("\033[0;30;42mParabens! Voce acertou.\033[m")
    print("-=-" * 20)
else:
    print("-=-" * 20)
    print(
        f"\033[0;32;41mERROU! Pensei no Numero {numero_computador} é não no {palpite}\033[m")
    print("-=-" * 20)
