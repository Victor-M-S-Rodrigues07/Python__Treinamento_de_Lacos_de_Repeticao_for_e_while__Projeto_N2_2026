contador = 10

def contagem_regressiva():

    for contador_this in range (contador, 0, -1):

        if contador_this % 2 == 0:

            print (f"Faltam apenas {contador_this} segundos - Não perca essa oportunidade!")
        
        else:

            print (f"A contagem continua: {contador_this} segundos restantes.")
    
    print ("Aproveite a promoção agora!")

contagem_regressiva()