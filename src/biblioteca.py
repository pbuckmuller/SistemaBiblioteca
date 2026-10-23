from datetime import datetime, timedelta

from src.banco import Banco
from src.livro import Livro
from src.usuario import Usuario
from src.emprestimo import Emprestimo


class Biblioteca:
    def __init__(self, banco: Banco):
        self.banco = banco
        self.livros: list[Livro] = []
        self.usuarios: list[Usuario] = []
        self.emprestimos: list[Emprestimo] = []

    def carregar_livros(self) -> None:
        livros = self.banco.buscar_livros()

        for id_livro, titulo, autor in livros:
            livro = Livro(id_livro, titulo, autor)
            self.livros.append(livro)

    def carregar_usuarios(self) -> None:
        usuarios = self.banco.buscar_usuarios()

        for id_usuario, nome, contato in usuarios:
            usuario = Usuario(id_usuario, nome, contato)
            self.usuarios.append(usuario)

    def carregar_emprestimos(self) -> None:
        emprestimos = self.banco.buscar_emprestimos()

        for (
                id_emprestimo,
                id_usuario,
                id_livro,
                data_emprestimo,
                data_prevista_devolucao,
                data_devolucao
        ) in emprestimos:

            usuario = self.buscar_usuario(id_usuario)
            livro = self.buscar_livro(id_livro)

            if usuario is None or livro is None:
                continue

            data_emprestimo = datetime.fromisoformat(data_emprestimo)
            data_prevista_devolucao = datetime.fromisoformat(data_prevista_devolucao)

            if data_devolucao is not None:
                data_devolucao = datetime.fromisoformat(data_devolucao)

            emprestimo = Emprestimo(
                id_emprestimo,
                usuario,
                livro,
                data_emprestimo,
                data_prevista_devolucao,
                data_devolucao
            )

            self.emprestimos.append(emprestimo)

    def cadastrar_livro(self, titulo: str, autor: str) -> Livro:
        id_livro = self.banco.inserir_livro(titulo, autor)

        livro = Livro(id_livro, titulo, autor)
        self.livros.append(livro)

        return livro

    def cadastrar_usuario(self, nome: str, contato: str) -> Usuario:
        id_usuario = self.banco.inserir_usuario(nome, contato)

        usuario = Usuario(id_usuario, nome, contato)
        self.usuarios.append(usuario)

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

            id_emprestimo = self.banco.inserir_emprestimo(
                usuario.id_usuario,
                livro.id_livro,
                data_emprestimo.isoformat(),
                data_prevista_devolucao.isoformat()
            )

            emprestimo = Emprestimo(
                id_emprestimo,
                usuario,
                livro,
                data_emprestimo,
                data_prevista_devolucao
            )

            self.emprestimos.append(emprestimo)

            return True

        return False

    def realizar_devolucao(self, emprestimo: Emprestimo) -> bool:
        if emprestimo.esta_ativo():
            emprestimo.registrar_devolucao()

            self.banco.registrar_devolucao(
                emprestimo.id_emprestimo,
                emprestimo.data_devolucao.isoformat()
            )

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
                return False

        self.banco.remover_livro(livro.id_livro)
        self.livros.remove(livro)

        return True

    def remover_usuario(self, usuario: Usuario) -> bool:
        for emprestimo in self.emprestimos:
            if usuario.id_usuario == emprestimo.id_usuario and emprestimo.esta_ativo():
                return False

        self.banco.remover_usuario(usuario.id_usuario)
        self.usuarios.remove(usuario)

        return True