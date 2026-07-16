lista_livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]

def listar_livros(lista):

    for livro_atual in lista:

        if livro_atual["estoque"] == 0:

            continue

        else:

            print (f"Livro disponível: {livro_atual["nome"]}")

listar_livros(lista_livros)

# Acessa o dicionário usando []