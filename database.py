import sqlite3

print("Conectando ao banco de dados...")
conn = sqlite3.connect('DBpy.db')
cursor = conn.cursor()
print("Conexão estabelecida")

#cursor.execute('''CREATE TABLE IF NOT EXISTS Alunos (id INTEGER PRIMARY KEY, nome TEXT, data_de_nascimento TEXT)''')
cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (id INTEGER PRIMARY KEY, produto TEXT, quantidade INTEGER, codigo NUMERIC)''')

print("Tabela criada com sucesso")