lista_cliente = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

def exibir_clientes():

    contador = 0

    for nome_cliente_atual in lista_cliente:

        contador = contador + 1

        print (f"Cliente Nº {contador}: {nome_cliente_atual}")
    
exibir_clientes()