from datetime import datetime, timedelta


def carregar_dados_teste(biblioteca):
    biblioteca.cadastrar_livro("O Hobbit", "J. R. R. Tolkien")
    biblioteca.cadastrar_livro("1984", "George Orwell")
    biblioteca.cadastrar_livro("Dom Casmurro", "Machado de Assis")
    biblioteca.cadastrar_livro("Clean Code", "Robert C. Martin")
    biblioteca.cadastrar_livro("O Guia do Mochileiro das Galáxias", "Douglas Adams")

    biblioteca.cadastrar_usuario("Pedro Henrique", "pedro@email.com")
    biblioteca.cadastrar_usuario("Ana Clara", "aninha@email.com")
    biblioteca.cadastrar_usuario("Marcos Silva", "marquitos@email.com")


class Livro:
    def __init__(self, id_livro: int, titulo: str, autor: str):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id_livro} | {self.titulo} | {self.autor}"


class Usuario:
    def __init__(self, id_usuario: int, nome: str, contato: str):
        self.id_usuario = id_usuario
        self.nome = nome
        self.contato = contato

    def __str__(self):
            return f"ID: {self.id_usuario} | {self.nome} | {self.contato}"


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

