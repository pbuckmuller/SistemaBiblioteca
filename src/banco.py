import sqlite3


class Banco:
    def __init__(self, caminho: str = "biblioteca.db"):
        self.caminho = caminho
        self.conexao = sqlite3.connect(caminho)

    def criar_tabelas(self) -> None:
        cursor = self.conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS livros (
                id_livro INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                autor TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id_usuario INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                contato TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS emprestimos (
                id_emprestimo INTEGER PRIMARY KEY AUTOINCREMENT,
                id_usuario INTEGER NOT NULL,
                id_livro INTEGER NOT NULL,
                data_emprestimo TEXT NOT NULL,
                data_prevista_devolucao TEXT NOT NULL,
                data_devolucao TEXT,
                FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
                FOREIGN KEY (id_livro) REFERENCES livros(id_livro)
            )
        """)

        self.conexao.commit()

    def inserir_emprestimo(
            self,
            id_usuario: int,
            id_livro: int,
            data_emprestimo: str,
            data_prevista_devolucao: str
    ) -> int:
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            INSERT INTO emprestimos (
                id_usuario,
                id_livro,
                data_emprestimo,
                data_prevista_devolucao
            )
            VALUES (?, ?, ?, ?)
            """,
            (
                id_usuario,
                id_livro,
                data_emprestimo,
                data_prevista_devolucao
            )
        )

        self.conexao.commit()
        return cursor.lastrowid

    def inserir_livro(self, titulo: str, autor: str) -> int:
        cursor = self.conexao.cursor()

        cursor.execute(
            "INSERT INTO livros (titulo, autor) VALUES (?, ?)",
            (titulo, autor)
        )

        self.conexao.commit()
        return cursor.lastrowid

    def inserir_usuario(self, nome: str, contato: str) -> int:
        cursor = self.conexao.cursor()

        cursor.execute(
            "INSERT INTO usuarios (nome, contato) VALUES (?, ?)",
            (nome, contato)
        )

        self.conexao.commit()
        return cursor.lastrowid

    def buscar_livros(self) -> list[tuple]:
        cursor = self.conexao.cursor()

        cursor.execute(
            "SELECT id_livro, titulo, autor FROM livros"
        )

        return cursor.fetchall()

    def buscar_usuarios(self) -> list[tuple]:
        cursor = self.conexao.cursor()

        cursor.execute(
            "SELECT id_usuario, nome, contato FROM usuarios"
        )

        return cursor.fetchall()

    def buscar_emprestimos(self) -> list[tuple]:
        cursor = self.conexao.cursor()
        cursor.execute(
            """
            SELECT
                id_emprestimo,
                id_usuario,
                id_livro,
                data_emprestimo,
                data_prevista_devolucao,
                data_devolucao
            FROM emprestimos
            """
        )
        return cursor.fetchall()

    def registrar_devolucao(
            self,
            id_emprestimo: int,
            data_devolucao: str
    ) -> None:
        cursor = self.conexao.cursor()

        cursor.execute(
            """
            UPDATE emprestimos
            SET data_devolucao = ?
            WHERE id_emprestimo = ?
            """,
            (data_devolucao, id_emprestimo)
        )

        self.conexao.commit()

    def remover_livro(self, id_livro: int) -> None:
        cursor = self.conexao.cursor()

        cursor.execute(
            "DELETE FROM livros WHERE id_livro = ?",
            (id_livro,)
        )

        self.conexao.commit()

    def remover_usuario(self, id_usuario: int) -> None:
        cursor = self.conexao.cursor()

        cursor.execute(
            "DELETE FROM usuarios WHERE id_usuario = ?",
            (id_usuario,)
        )

        self.conexao.commit()

    def fechar(self) -> None:
        self.conexao.close()