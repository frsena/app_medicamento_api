from datetime import datetime
import sqlite3


print("Conectando...")

db_path = "database/"

conn = sqlite3.connect('database//db.sqlite3')

conn.execute('delete from remedio')
conn.commit()

# inserindo jogos
sql = 'INSERT INTO remedio (nome, data_insercao) VALUES (?,?)'

dados = [
      ('Nesoldina', datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Discongex", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Multigrip", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
      ("Novalgina", datetime.now().strftime("%Y-%m-%d %H:%M:%S")), 
]



conn.executemany(sql, dados)
conn.commit()
conn.close()