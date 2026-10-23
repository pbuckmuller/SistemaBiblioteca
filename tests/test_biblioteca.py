from src.biblioteca import Biblioteca


def test_cadastrar_livro():
    biblioteca = Biblioteca()

    livro = biblioteca.cadastrar_livro("O Guia do Mochileiro das Galáxias", "Douglas Adams")

    assert len(biblioteca.livros) == 1
    assert livro.titulo == "O Guia do Mochileiro das Galáxias"
    assert livro.autor == "Douglas Adams"

def test_livro_emprestado_indisponivel():
    biblioteca = Biblioteca()

    usuario1 = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    usuario2 = biblioteca.cadastrar_usuario("Bruno Lopes", "19-023456785")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    assert biblioteca.realizar_emprestimo(usuario1, livro)
    assert not biblioteca.realizar_emprestimo(usuario2, livro)

def test_livro_devolvido_disponivel():
    biblioteca = Biblioteca()

    usuario1 = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    usuario2 = biblioteca.cadastrar_usuario("Bruno Lopes", "19-023456785")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    assert biblioteca.realizar_emprestimo(usuario1, livro)
    assert biblioteca.realizar_devolucao(biblioteca.emprestimos[0])
    assert biblioteca.realizar_emprestimo(usuario2, livro)

def test_remocao_livro():
    biblioteca = Biblioteca()

    usuario = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    livro1 = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")
    livro2 = biblioteca.cadastrar_livro("O Guia do Mochileiro das Galáxias", "Douglas Adams")

    biblioteca.realizar_emprestimo(usuario, livro2)

    assert biblioteca.remover_livro(livro1)
    assert not biblioteca.remover_livro(livro2)

def test_remocao_usuario():
    biblioteca = Biblioteca()

    usuario1 = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    usuario2 = biblioteca.cadastrar_usuario("Bruno Lopes", "19-023456785")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    biblioteca.realizar_emprestimo(usuario2, livro)

    assert biblioteca.remover_usuario(usuario1)
    assert not biblioteca.remover_usuario(usuario2)

def test_emprestimo_ja_devolvido():
    biblioteca = Biblioteca()

    usuario = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    biblioteca.realizar_emprestimo(usuario, livro)
    assert biblioteca.realizar_devolucao(biblioteca.emprestimos[0])
    assert not biblioteca.realizar_devolucao(biblioteca.emprestimos[0])

