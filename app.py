while True:
    # Usuário deve informar o seu tipo de imóvel
    imovel_U = input(
        "Qual o seu tipo de Imóvel? (Casa, Apartamento ou Comercial): ").strip().lower()

    # Usuário deve informar o consumo em metros cúbicos de água
    Consumo_U = float(input("Qual o seu consumo em metros cúbicos de água? (m³): "))

    # Seção dos imóveis residenciais: Casas e Apartamentos
    if imovel_U == "apartamento" or imovel_U == "casa":

        if Consumo_U <= 10:
            print("Consumo econômico - excelente controle de água!")

        elif Consumo_U <= 25:
            print("Consumo moderado - dentro do padrão residencial.")

        else:
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")

    # Seção dos imóveis comerciais
    elif imovel_U == "comercial":

        if Consumo_U <= 10:
            print("Consumo econômico - excelente controle de água!")
            print("Consulte o plano corporativo")

        elif Consumo_U <= 25:
            print("Consumo moderado - dentro do padrão residencial.")
            print("Consulte o plano corporativo")

        else:
            print("Consumo excessivo - adote medidas de economia e verifique vazamentos.")
            print("Consulte o plano corporativo")

    # Caso o usuário digite um imóvel diferente
    else:
        print("Tipo de imóvel inválido.")

    resposta = input("Deseja refazer a classificação de consumo? (Sim ou não):").strip().lower()
    if resposta == "sim" or resposta == "s":
        continue
    else:
        print("programa encerrado")
        break

