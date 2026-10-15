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
            "6 - Listar usuários\n"
            "7 - Listar empréstimos\n"
            "8 - Remover livro\n"
            "9 - Remover usuário\n"
            "0 - Sair\n"
            )

        opcao = None

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

                situacao = biblioteca.realizar_emprestimo(usuario, livro)
                if situacao:
                    print(f"\nEmpréstimo aprovado!")
                else:
                    print(f"\nEsse livro está indisponível para empréstimo no momento.")

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
                while True:
                    try:
                        id_digitado = int(input("Digite o ID do livro a ser removido: "))
                    except ValueError:
                        print("Por favor, digite somente um número inteiro válido.")
                        continue
                    livro = biblioteca.buscar_livro(id_digitado)
                    if livro is None:
                        print("O ID digitado não corresponde a nenhum livro da biblioteca")
                        continue
                    resultado = biblioteca.remover_livro(livro)
                    if resultado:
                        print("Livro removido com sucesso!")
                        break
                    else:
                        print("O livro não pode ser removido pois possui um empréstimo ativo.")
                        break
            
            elif opcao == 9:
                while True:
                    try:
                        id_digitado = int(input("Digite o ID do usuário a ser removido: "))
                    except ValueError:
                        print("Por favor, digite somente um número inteiro válido.")
                        continue
                    usuario = biblioteca.buscar_usuario(id_digitado)
                    if usuario is None:
                        print("O ID digitado não corresponde a nenhum usuário cadastrado no sistema.")
                        continue
                    resultado = biblioteca.remover_usuario(usuario)
                    if resultado:
                        print("Usuário removido com sucesso!")
                        break
                    else:
                        print("O usuário não pode ser removido pois possui um empréstimo ativo.")
                        break

            else:
                print("Por favor, digite uma opção válida.")

        except ValueError:
            print("Por favor, digite uma opção válida.")

if __name__ == "__main__":
    main()

