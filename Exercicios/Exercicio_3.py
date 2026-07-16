def exibir_mensagem():

    try:

        numero_repeticoes = int (input ("Digite o número de repetições da mensagem: "))

        for indice in range(numero_repeticoes):

            print ("Bem vindo ao Buscante!")
            indice += 1

    except ValueError:

        print ("Somente números inteiros são permitidos")
        exibir_mensagem()

exibir_mensagem()