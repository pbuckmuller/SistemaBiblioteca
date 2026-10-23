class Livro:
    def __init__(self, id_livro: int, titulo: str, autor: str):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id_livro} | {self.titulo} | {self.autor}"