class Autor:
    def __init__(self, nome, data_nascimento):
        self.nome = nome
        self.data_nascimento = data_nascimento

class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor


autor1 = Autor("J.K. Rowling", "31 de julho de 1965")
livro1 = Livro("Harry Potter e a Pedra Filosofal", autor1)

print(f"Autor: {livro1.autor.nome}")
print(f"Data de Nascimento do Autor: {livro1.autor.data_nascimento}")
print(f"Título do Livro: {livro1.titulo}")