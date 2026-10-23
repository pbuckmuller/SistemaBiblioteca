from datetime import datetime, timedelta

from src.livro import Livro
from src.usuario import Usuario
from src.emprestimo import Emprestimo


class Biblioteca:
    def __init__(self):
        self.livros: list[Livro] = []
        self.usuarios: list[Usuario] = []
        self.emprestimos: list[Emprestimo] = []
        self.proximo_id_emprestimo = 1
        self.proximo_id_livro = 1
        self.proximo_id_usuario = 1

    def cadastrar_livro(self, titulo: str, autor: str) -> Livro:
        livro = Livro(self.proximo_id_livro, titulo, autor)
        self.livros.append(livro)
        self.proximo_id_livro += 1
        return livro

    def cadastrar_usuario(self, nome: str, contato: str) -> Usuario:
        usuario = Usuario(self.proximo_id_usuario, nome, contato)
        self.usuarios.append(usuario)
        self.proximo_id_usuario += 1
        return usuario

    def livro_esta_disponivel(self, livro: Livro) -> bool:
        for e in self.emprestimos:
            if livro.id_livro == e.id_livro and e.esta_ativo():
                return False

        return True

    def realizar_emprestimo(self, usuario: Usuario, livro: Livro) -> bool:
        if self.livro_esta_disponivel(livro):
            data_emprestimo = datetime.now()
            data_prevista_devolucao = data_emprestimo + timedelta(days=30)
            emprestimo = Emprestimo(self.proximo_id_emprestimo, usuario, livro, data_emprestimo, data_prevista_devolucao)
            self.emprestimos.append(emprestimo)
            self.proximo_id_emprestimo += 1
            return True

        return False

    def realizar_devolucao(self, emprestimo: Emprestimo) -> bool:
        if emprestimo.esta_ativo():
            emprestimo.registrar_devolucao()
            return True

        return False

    def buscar_usuario(self, id_usuario: int) -> Usuario | None:
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario
        return None

    def buscar_livro(self, id_livro: int) -> Livro | None:
        for livro in self.livros:
            if livro.id_livro == id_livro:
                return livro
        return None

    def buscar_emprestimo(self, id_emprestimo: int) -> Emprestimo | None:
        for emprestimo in self.emprestimos:
            if emprestimo.id_emprestimo == id_emprestimo:
                return emprestimo
        return None

    def remover_livro(self, livro: Livro) -> bool:
        for emprestimo in self.emprestimos:
            if livro.id_livro == emprestimo.id_livro and emprestimo.esta_ativo():
                # remoção não acontece
                return False
        # não encontrou barreiras no for? remoção aprovada!
        self.livros.remove(livro)
        return True

    def remover_usuario(self, usuario: Usuario) -> bool:
        for emprestimo in self.emprestimos:
            if usuario.id_usuario == emprestimo.id_usuario and emprestimo.esta_ativo():
                # não remove usuario
                return False
        # usuario não tem emprestimo ativo? então podemos remover!
        self.usuarios.remove(usuario)
        return True