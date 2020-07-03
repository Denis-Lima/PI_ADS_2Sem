import sqlite3 as sql

#conectando
conn = sql.connect('clientes.db')

#definindo cursor
cursor = conn.cursor()

#criando tabela
cursor.execute("""
CREATE TABLE clientes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL);""")

#desconectando
conn.close
