class Usuario:
    def __init__(self, id_usuario: int, nome: str, contato: str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.contato = contato

    def __str__(self):
            return f"ID: {self.id_usuario} | {self.nome} | {self.contato}"