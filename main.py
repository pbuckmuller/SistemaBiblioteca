from classes import *


LARGURA = 40


def main():
    biblioteca = Biblioteca()

    carregar_dados_teste(biblioteca)

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
            "6 - Listar usuarios\n"
            "7 - Listar empréstimos\n"
            "0 - Sair\n"
            )

        opcao = None

        try:
            opcao = int(input("Escolha uma opção: "))

            if opcao == 0:
                break
        
            elif opcao == 1:
                titulo = input("Digite o título: ").strip()
                autor = input("Digite o autor: ").strip()
                biblioteca.cadastrar_livro(titulo, autor)
                print(f"O seguinte livro foi cadastrado: {titulo} | Autor: {autor}")

            elif opcao == 2:
                nome = input("Digite seu nome: ").strip()
                contato = input("Digite seu email ou telefone: ").strip()
                biblioteca.cadastrar_usuario(nome, contato)
                print(f"O seguinte usuário foi cadastrado: {nome} | Contato: {contato}")

            elif opcao == 3:
                usuario = None
                livro = None

                while usuario is None:
                    try:
                        id_usuario = int(input("Digite seu ID de usuário: "))
                        usuario = biblioteca.buscar_usuario(id_usuario)
                        if usuario is None:
                            print("Digite um ID de usuário válido")
                    except ValueError:
                        print("Digite um ID válido.")

                while livro is None:
                    try:
                        id_livro = int(input("Digite o ID do livro: "))
                        livro = biblioteca.buscar_livro(id_livro)
                        if livro is None:
                            print("Digite um ID de livro válido")
                    except ValueError:
                        print("Digite um ID válido.")

                biblioteca.realizar_emprestimo(usuario, livro)
                

            elif opcao == 4:
                emprestimo = None

                while emprestimo is None:
                    try:
                        id_emprestimo= int(input("Digite o ID do empréstimo: "))
                        emprestimo = biblioteca.buscar_emprestimo(id_emprestimo)

                        if emprestimo is None:
                            print("Digite um ID de empréstimo válido")
                    except ValueError:
                        print("Digite um ID válido.")

                biblioteca.realizar_devolucao(emprestimo)

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

            else:
                print("Por favor, digite uma opção válida.")

        except ValueError:
            print("Por favor, digite uma opção válida.")

if __name__ == "__main__":
    main()

