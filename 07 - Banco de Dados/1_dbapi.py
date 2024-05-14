import sqlite3
from pathlib import Path

import mysql.connector

ROOT_PATH = Path(__file__).parent

# CONEXÃO SQLITE
conexao = sqlite3.connect(ROOT_PATH / "meu_banco.sqlite")
# print(conexao)

# CONEXÃO MYSQL
my_con = mysql.connector.connect(
    host="localhost", user="root", password="admin", database="boabiblioteca"
)
# print(my_con)

cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row


def mostrar_bancos(cursor):
    cursor.execute("SHOW DATABASES")
    for x in cursor:
        print(x)


def criar_tabela(conexao, cursor):
    cursor.execute(
        "CREATE TABLE clientes (id INTEGER PRIMARY KEY AUTOINCREMENT, nome VARCHAR(100), email VARCHAR(150))"
    )
    conexao.commit()


def inserir_registro(conexao, cursor, nome, email):
    data = (nome, email)
    # cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", (nome, email))
    cursor.execute("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


def atualizar_registro(conexao, cursor, nome, email, id):
    data = (nome, email, id)
    cursor.execute("UPDATE clientes SET nome = ?, email = ? WHERE id = ?", data)
    conexao.commit()


def excluir_registro(conexao, cursor, id):
    data = (id,)
    cursor.execute("DELETE FROM clientes WHERE id = ?", data)
    conexao.commit()


def inserir_muitos(conexao, cursor, data):
    cursor.executemany("INSERT INTO clientes (nome, email) VALUES (?,?);", data)
    conexao.commit()


def recuperar_cliente(cursor, id):
    cursor.execute("SELECT email, id, nome FROM clientes WHERE id=?", (id,))
    return cursor.fetchone()


def listar_clientes(cursor):
    cursor.execute("SELECT * FROM clientes ORDER BY nome DESC;")
    return cursor.fetchall()


clientes = listar_clientes(cursor)
for cliente in clientes:
    print(dict(cliente))

# cliente = recuperar_cliente(cursor, 2)
# print(dict(cliente))
# print(cliente["id"], cliente["nome"], cliente["email"])
# print(f'Seja bem vindo ao sistema {cliente["nome"]}')


# dados = [
#     ("Teste", "teste@teste.com"),
#     ("Sicrano", "sicrano@sicrano.com"),
#     ("Beltrano", "beltrano@beltrano.com"),
# ]

# inserir_muitos(conexao, cursor, dados)
