import random
from time import sleep

print("Escolha uma das opções")
print("1 - PEDRA")
print("2 - PAPEL")
print("3 - TESOURA")
print("4 - Sair do jogo")

opcao_jogador = int(input("Digite uma opção de (1/2/3/4): "))
print("\033[1;33;47mCARREGANDO...\033[m")
sleep(2)

if opcao_jogador == 4:
    print("\033[1;31;47mSAIU DO JOGO\033[m")
else:
    computador = random.randint(1, 3)
    nomes = {1: "Pedra", 2: "Papel", 3: "Tesoura"}

    if opcao_jogador == computador:
        print(f"EMPATE! {nomes[opcao_jogador]} com {nomes[computador]}")
    elif opcao_jogador == 1 and computador == 2:
        print("GANHEI! Papel ganha de Pedra")
    elif opcao_jogador == 1 and computador == 3:
        print("Você Ganhou! Pedra ganha de Tesoura")
    elif opcao_jogador == 2 and computador == 1:
        print("Você Ganhou! Papel ganha de Pedra")
    elif opcao_jogador == 2 and computador == 3:
        print("GANHEI! Tesoura ganha de Papel")
    elif opcao_jogador == 3 and computador == 1:
        print("GANHEI! Pedra ganha de Tesoura")
    elif opcao_jogador == 3 and computador == 2:
        print("Você Ganhou! Tesoura ganha de Papel")
    else:
        print("Opção inválida!")

    print(
        f"Escolhi {nomes[computador]} enquanto você escolheu {nomes.get(opcao_jogador, 'Opção inválida')}")
# .get() procura uma chave no dicionário e retorna o valor dela.
# Se a chave não existir, retorna None ou o valor que eu definir.
