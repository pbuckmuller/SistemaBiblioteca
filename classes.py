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
    def __init__(self, id_livro, titulo, autor):
        self.id_livro = id_livro
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"ID: {self.id_livro} | {self.titulo} | {self.autor}"


class Usuario:
    def __init__(self, id_usuario, nome, contato):
        self.id_usuario = id_usuario
        self.nome = nome
        self.contato = contato

    def __str__(self):
            return f"ID: {self.id_usuario} | {self.nome} | {self.contato}"


class Emprestimo:
    def __init__(self, id_emprestimo, usuario, livro, data_emprestimo, data_prevista_devolucao, data_devolucao = None):
        self.id_emprestimo = id_emprestimo
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = data_emprestimo
        self.data_prevista_devolucao = data_prevista_devolucao
        self.data_devolucao = data_devolucao

    def registrar_devolucao(self):
        data_devolucao = datetime.now()
        self.data_devolucao = data_devolucao

    def esta_ativo(self):
        if self.data_devolucao is None:
            return True

        else:
            return False

    def __str__(self):
        data_emprestimo = self.data_emprestimo.strftime("%d/%m/%Y")
        data_prevista_devolucao = self.data_prevista_devolucao.strftime("%d/%m/%Y")
        
        if self.data_devolucao is None:
            status = "Ativo"
        else:
            data_devolucao = self.data_devolucao.strftime("%d/%m/%Y")
            status = f"Devolvido em {data_devolucao}"
            
        return (
            f"ID do empréstimo: {self.id_emprestimo}\n"
            f"Usuário: {self.usuario.nome} (ID: {self.usuario.id_usuario})\n"
            f"Livro: {self.livro.titulo} (ID: {self.livro.id_livro})\n"
            f"Data do empréstimo: {data_emprestimo}\n"
            f"Devolução prevista: {data_prevista_devolucao}\n"
            f"Status: {status}"
        )


class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []
        self.emprestimos = []
        self.proximo_id_emprestimo = 1
        self.proximo_id_livro = 1
        self.proximo_id_usuario = 1

    def cadastrar_livro(self, titulo , autor):
        livro = Livro(self.proximo_id_livro, titulo, autor)
        self.livros.append(livro)
        self.proximo_id_livro += 1

    def cadastrar_usuario(self, nome, contato):
        usuario = Usuario(self.proximo_id_usuario, nome, contato)
        self.usuarios.append(usuario)
        self.proximo_id_usuario += 1

    def livro_esta_disponivel(self, livro):
        for e in self.emprestimos:
            
            if livro == e.livro:

                if e.esta_ativo():
                    return False

        return True

    def realizar_emprestimo(self, usuario, livro):
        if self.livro_esta_disponivel(livro):
            data_emprestimo = datetime.now()
            data_prevista_devolucao = data_emprestimo + timedelta(days=30)
            emprestimo = Emprestimo(self.proximo_id_emprestimo, usuario, livro, data_emprestimo, data_prevista_devolucao)
            self.emprestimos.append(emprestimo)
            self.proximo_id_emprestimo += 1
            print()
            print(f"Empréstimo aprovado!")

        else:
            print()
            print(f"Esse livro está indisponível para empréstimo no momento.")
    
    def realizar_devolucao(self, emprestimo):
        if emprestimo.esta_ativo():
            emprestimo.registrar_devolucao()
            print()
            print(f"Devolução confirmada!")
                
        else:
            print("Esse empréstimo já foi devolvido")

    def buscar_usuario(self, id_usuario:int):
        for usuario in self.usuarios:
            if usuario.id_usuario == id_usuario:
                return usuario

    def buscar_livro(self, id_livro:int):
        for livro in self.livros:
            if livro.id_livro == id_livro:
                return livro
        
    def buscar_emprestimo(self, id_emprestimo:int):
        for emprestimo in self.emprestimos:
            if emprestimo.id_emprestimo == id_emprestimo:
                return emprestimo

