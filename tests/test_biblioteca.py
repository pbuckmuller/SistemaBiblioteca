from src.banco import Banco
from src.biblioteca import Biblioteca

import pytest


@pytest.fixture
def banco():
    banco = Banco(":memory:")
    banco.criar_tabelas()
    return banco


@pytest.fixture
def biblioteca(banco):
    return Biblioteca(banco)

def test_cadastrar_livro(biblioteca):
    livro = biblioteca.cadastrar_livro("O Guia do Mochileiro das Galáxias", "Douglas Adams")

    assert len(biblioteca.livros) == 1
    assert livro.titulo == "O Guia do Mochileiro das Galáxias"
    assert livro.autor == "Douglas Adams"

def test_livro_emprestado_indisponivel(biblioteca):
    usuario1 = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    usuario2 = biblioteca.cadastrar_usuario("Bruno Lopes", "19-023456785")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    assert biblioteca.realizar_emprestimo(usuario1, livro)
    assert not biblioteca.realizar_emprestimo(usuario2, livro)

def test_livro_devolvido_disponivel(biblioteca):
    usuario1 = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    usuario2 = biblioteca.cadastrar_usuario("Bruno Lopes", "19-023456785")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    assert biblioteca.realizar_emprestimo(usuario1, livro)
    assert biblioteca.realizar_devolucao(biblioteca.emprestimos[0])
    assert biblioteca.realizar_emprestimo(usuario2, livro)

def test_remocao_livro(biblioteca):
    usuario = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    livro1 = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")
    livro2 = biblioteca.cadastrar_livro("O Guia do Mochileiro das Galáxias", "Douglas Adams")

    biblioteca.realizar_emprestimo(usuario, livro2)

    assert biblioteca.remover_livro(livro1)
    assert not biblioteca.remover_livro(livro2)

def test_remocao_usuario(biblioteca):
    usuario1 = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    usuario2 = biblioteca.cadastrar_usuario("Bruno Lopes", "19-023456785")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    biblioteca.realizar_emprestimo(usuario2, livro)

    assert biblioteca.remover_usuario(usuario1)
    assert not biblioteca.remover_usuario(usuario2)

def test_emprestimo_ja_devolvido(biblioteca):
    usuario = biblioteca.cadastrar_usuario("Paloma Gonçalves", "11-123456789")
    livro = biblioteca.cadastrar_livro("Como domar um lobo", "Fulano de Tal")

    biblioteca.realizar_emprestimo(usuario, livro)
    assert biblioteca.realizar_devolucao(biblioteca.emprestimos[0])
    assert not biblioteca.realizar_devolucao(biblioteca.emprestimos[0])

def test_persistencia_livro(banco, biblioteca):
    livro = biblioteca.cadastrar_livro(
        "O Guia do Mochileiro das Galáxias",
        "Douglas Adams"
    )

    nova_biblioteca = Biblioteca(banco)
    nova_biblioteca.carregar_livros()

    livro_carregado = nova_biblioteca.buscar_livro(livro.id_livro)

    assert livro_carregado is not None
    assert livro_carregado.titulo == "O Guia do Mochileiro das Galáxias"
    assert livro_carregado.autor == "Douglas Adams"