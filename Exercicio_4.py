def somatoria_lista():

    lista_valores = [60, 80, 190, 540, 32, 100, 23, 40]
    soma = 0
    for numero in lista_valores:

        soma += numero
        print (f"A soma é {soma}")
    
    print (f"\nO resultado final é {soma}")

somatoria_lista()