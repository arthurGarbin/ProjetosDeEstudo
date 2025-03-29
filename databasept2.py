import sqlite3

print("Conectando ao banco de dados...")
conn = sqlite3.connect('DBpy.db')
cursor = conn.cursor()
print("Conexão estabelecida")

for i in range(3):
    nome = input("Digite seu nome: ")
    nasc = input("Digite sua data de nascimento (xx/xx/xxxx): ")
    cursor.execute('''INSERT INTO Alunos (nome, data_de_nascimento) VALUES (?, ?)''', (nome, nasc))
    conn.commit()

print("Dados inseridos com sucesso")