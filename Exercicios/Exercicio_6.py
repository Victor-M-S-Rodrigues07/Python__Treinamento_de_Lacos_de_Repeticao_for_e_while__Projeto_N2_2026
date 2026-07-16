lista_livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]

def buscar_livro (livro_procurado):

    contador = 0

    for livro_indice in lista_livros:

        contador += 1

        if livro_indice == livro_procurado:

            print (f"Livro encontrado! Estante Nº{contador}")
            break
    
    if contador == len (lista_livros):
        print ("Livro não encontrado ou indisponível")

livro_usuario = input ("Digite o nome do livro a ser procurado: ")

buscar_livro (livro_usuario)