import sqlite3 as sql

conn = sql.connect('clientes.db')

cursor = conn.cursor()

#inserindo dados
cursor.execute("""
INSERT INTO clientes(email)
    VALUES ('israel.santos13@fatec.sp.gov.br')""")

cursor.execute("""
INSERT INTO clientes(email)
    VALUES ('wesley.dias3@fatec.sp.gov.br')""")

cursor.execute("""
INSERT INTO clientes(email)
    VALUES ('denis.lima6@fatec.sp.gov.br')""")

cursor.execute("""
INSERT INTO clientes(email)
    VALUES ('natalia.biscaro@fatec.sp.gov.br')""")

conn.commit()

conn.close()
