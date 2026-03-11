exemplares_restantes = 5

def exibir_venda(exemplares):

    if exemplares != 0:

        while exemplares != 0:

            exemplares -= 1
            print (f"Venda realizada! Exemplares restantes: {exemplares}")
        
        exibir_venda(exemplares)
        
    else:

        print ("Acabaram as cópias, estoque esgotado!")

exibir_venda(exemplares_restantes)