from src.banco import Banco
from src.biblioteca import Biblioteca
from typing import TypeVar, Callable

T = TypeVar("T")
LARGURA = 40

def buscar_objeto(msg_input, msg_erro, funcao_buscar: Callable[[int], T | None]) -> T:
    resultado = None

    while resultado is None:
        try:
            dado = int(input(msg_input))
            resultado = funcao_buscar(dado)
            if resultado is None:
                print(msg_erro)
        except ValueError:
            print(msg_erro)
    return resultado

def main():
    banco = Banco()
    banco.criar_tabelas()

    biblioteca = Biblioteca(banco)
    biblioteca.carregar_livros()
    biblioteca.carregar_usuarios()
    biblioteca.carregar_emprestimos()

    print("=" * LARGURA)
    print("SISTEMA DA BIBLIOTECA".center(LARGURA))
    print("=" * LARGURA)

    while True:
        print(
            "\n1 - Cadastrar livro\n"
            "2 - Cadastrar usuário\n"
            "3 - Realizar empréstimo\n"
            "4 - Realizar devolução\n"
            "5 - Listar livros\n"
            "6 - Listar usuários\n"
            "7 - Listar empréstimos\n"
            "8 - Remover livro\n"
            "9 - Remover usuário\n"
            "0 - Sair\n"
            )

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 0:
                break
        
            elif opcao == 1:
                titulo = None
                autor = None

                while titulo is None:
                    titulo = input("Digite o título: ").strip()
                    if titulo == "":
                        print("Não são permitidos títulos em branco.")
                        titulo = None
                while autor is None:
                    autor = input("Digite o autor: ").strip()
                    if autor == "":
                        print("Não são permitidos nomes de autores em branco.")
                        autor = None
                livro = biblioteca.cadastrar_livro(titulo, autor)
                print(f"O seguinte livro foi cadastrado: ID: {livro.id_livro} | Título: {livro.titulo} | Autor: {livro.autor}")

            elif opcao == 2:
                nome = None
                contato = None

                while nome is None:
                    nome = input("Digite seu nome: ").strip()
                    if nome == "":
                        print("Não são permitidos nomes em branco.")
                        nome = None
                while contato is None:
                    contato = input("Digite seu email ou telefone: ").strip()
                    if contato == "":
                        print("O campo contato não pode estar em branco.")
                        contato = None                
                usuario = biblioteca.cadastrar_usuario(nome, contato)
                print(f"O seguinte usuário foi cadastrado: ID: {usuario.id_usuario} | Nome: {usuario.nome} | Contato: {usuario.contato}")

            elif opcao == 3:
                usuario = buscar_objeto(
                    "Digite seu ID de usuário: ",
                    "Digite um ID de usuário válido",
                    biblioteca.buscar_usuario
                )
                livro = buscar_objeto(
                    "Digite o ID do livro: ",
                    "Digite um ID de livro válido",
                    biblioteca.buscar_livro
                )

                resultado = biblioteca.realizar_emprestimo(usuario, livro)
                if resultado:
                    print("\nEmpréstimo aprovado!")
                else:
                    print("\nEsse livro está indisponível para empréstimo no momento.")

            elif opcao == 4:
                emprestimo = buscar_objeto(
                    "Digite o ID do empréstimo: ",
                    "Digite um ID de empréstimo válido",
                    biblioteca.buscar_emprestimo
                )

                resultado = biblioteca.realizar_devolucao(emprestimo)

                if resultado:
                    print("Devolução confirmada!")
                else:
                    print("Esse empréstimo já foi devolvido")

            elif opcao == 5:
                print()
                print("<LISTAGEM DOS LIVROS>")
                print()
                for livro in biblioteca.livros:
                    print(livro)

            elif opcao == 6:
                print()
                print("<LISTAGEM DOS USUÁRIOS>")
                print()
                for usuario in biblioteca.usuarios:
                    print(usuario)

            elif opcao == 7:
                print()
                print("<LISTAGEM DOS EMPRÉSTIMOS>")
                for emprestimo in biblioteca.emprestimos:
                    print()
                    print(emprestimo)
            
            elif opcao == 8:
                livro = buscar_objeto(
                    "Digite o ID do livro a ser removido: ",
                    "Por favor, digite um ID válido.",
                    biblioteca.buscar_livro
                )
                resultado = biblioteca.remover_livro(livro)
                if resultado:
                    print("Livro removido com sucesso!")
                else:
                    print("O livro não pode ser removido pois possui um empréstimo ativo.")

            elif opcao == 9:
                usuario = buscar_objeto(
                    "Digite o ID do usuário a ser removido: ",
                    "Por favor, digite um ID válido.",
                    biblioteca.buscar_usuario
                )
                resultado = biblioteca.remover_usuario(usuario)
                if resultado:
                    print("Usuário removido com sucesso!")
                else:
                    print("O usuário não pode ser removido pois possui um empréstimo ativo.")

            else:
                print("Por favor, digite uma opção válida.")

        except ValueError:
            print("Por favor, digite uma opção válida.")

    banco.fechar()

if __name__ == "__main__":
    main()

