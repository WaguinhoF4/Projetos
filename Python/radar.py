velocidade_carro = int(
    input("\033[1;30;44mDigite a Velocidade do Carro: \033[m"))

if velocidade_carro > 80:
    print(
        "\033[0;31;41mMULTADO! Voce excedeu o limite que é permitido que é de 80km/h\033[m")
    multa = (velocidade_carro - 80) * 7
    print(f"\033[1;31;43mVoce deve pagar uma multa de R${multa:.2f}\033[m")
elif velocidade_carro <= 79:
    print(
        "\033[0;36;43mVoce está muito abaixo da velocidade da Via! Acelere um pouco mais!\033[m")
elif velocidade_carro == 80:
    print("\033[0;30;42mVoce esta na Velocidade da Via! Tenha um Bom dia! Dirija com segurança!\033[m")
