from datetime import datetime

from src.usuario import Usuario
from src.livro import Livro

class Emprestimo:
    def __init__(
            self,
            id_emprestimo: int,
            usuario: Usuario,
            livro: Livro,
            data_emprestimo: datetime,
            data_prevista_devolucao: datetime,
            data_devolucao: datetime | None = None
    ):
        self.id_emprestimo = id_emprestimo
        self.id_usuario = usuario.id_usuario
        self.nome_usuario = usuario.nome
        self.id_livro = livro.id_livro
        self.titulo_livro = livro.titulo
        self.autor_livro = livro.autor
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_devolucao = data_devolucao

    def registrar_devolucao(self) -> None:
        data_devolucao = datetime.now()
        self.data_devolucao = data_devolucao

    def esta_ativo(self) -> bool:
        if self.data_devolucao is None:
            return True
        return False

    def __str__(self) -> str:
        data_emprestimo = self.data_emprestimo.strftime("%d/%m/%Y")
        data_prevista_devolucao = self.data_prevista_devolucao.strftime("%d/%m/%Y")

        if self.data_devolucao is None:
            status = "Ativo"
        else:
            data_devolucao = self.data_devolucao.strftime("%d/%m/%Y")
            status = f"Devolvido em {data_devolucao}"

        return (
            f"ID do empréstimo: {self.id_emprestimo}\n"
            f"Usuário: {self.nome_usuario} (ID: {self.id_usuario})\n"
            f"Livro: {self.titulo_livro} (ID: {self.id_livro})\n"
            f"Data do empréstimo: {data_emprestimo}\n"
            f"Devolução prevista: {data_prevista_devolucao}\n"
            f"Status: {status}"
        )