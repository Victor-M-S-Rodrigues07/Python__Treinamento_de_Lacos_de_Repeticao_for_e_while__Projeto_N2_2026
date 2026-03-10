def exibir_portfolio():

    lista_projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
    contador = 0

    for proposta_atual in lista_projetos:

        if proposta_atual == None:

            print ("Projeto Ausente")
            continue

        contador += 1
        print (f"Projeto Nº {contador} - {proposta_atual}")

exibir_portfolio()