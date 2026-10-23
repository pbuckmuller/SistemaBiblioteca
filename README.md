# SistemaBiblioteca

Sistema de gerenciamento de biblioteca desenvolvido em Python como projeto de estudo e portfólio.

O projeto permite cadastrar livros e usuários, realizar empréstimos e devoluções, consultar registros e remover livros e usuários respeitando as regras do sistema.

## Funcionalidades

- Cadastro de livros
- Cadastro de usuários
- Realização de empréstimos
- Registro de devoluções
- Listagem de livros, usuários e empréstimos
- Remoção de livros e usuários
- Controle de disponibilidade dos livros
- Persistência dos dados utilizando SQLite
- Testes automatizados com pytest

## Tecnologias

- Python
- Programação Orientada a Objetos (POO)
- SQLite
- pytest
- Git e GitHub

## Estrutura do projeto

```text
SistemaBiblioteca/
├── src/
│   ├── __init__.py
│   ├── banco.py
│   ├── biblioteca.py
│   ├── emprestimo.py
│   ├── livro.py
│   └── usuario.py
├── tests/
│   └── test_biblioteca.py
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

## Como executar

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/pbuckmuller/SistemaBiblioteca.git
cd SistemaBiblioteca
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute o sistema:

```bash
python main.py
```

O banco de dados SQLite será criado automaticamente como `biblioteca.db`.

## Testes

Para executar os testes:

```bash
python -m pytest
```

O projeto possui testes para os principais comportamentos do sistema, incluindo cadastro, empréstimos, devoluções, remoções e persistência dos dados.

## Objetivo do projeto

Este projeto foi desenvolvido para praticar conceitos de Python e Programação Orientada a Objetos em uma aplicação funcional, além de introduzir testes automatizados e persistência de dados com SQLite.

O foco foi construir uma aplicação simples, organizada e funcional, evitando complexidade desnecessária.