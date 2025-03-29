'''
for i in range(3):
    nome = input("Nome: ")
'''

'''
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.withdraw()  # Esconde a janela principal

messagebox.showinfo("","Seu item já foi adicionado no banco de dados")

root.mainloop()
'''
'''
import sqlite3
import tkinter as tk
from tkinter import messagebox

# Função para obter dados do banco de dados
def get_data_from_db():
    # Conectar ao banco de dados (substitua 'meu_banco.db' pelo nome do seu banco de dados)
    conn = sqlite3.connect('DBpy.db')
    cursor = conn.cursor()
    
    # Executar uma consulta SQL (substitua 'minha_tabela' pelo nome da sua tabela e 'minha_coluna' pela coluna que deseja consultar)
    cursor.execute("SELECT * FROM produtos WHERE codigo")
    data = cursor.fetchone()
    
    # Fechar a conexão
    conn.close()
    
    return data[0] if data else None

# Crie a janela principal
root = tk.Tk()
root.geometry('500x500')
root.withdraw()  # Esconde a janela principal

# Obter dados do banco de dados
dados = get_data_from_db()

# Exibir os dados em uma messagebox
if dados:
    messagebox.showinfo("Dados do Banco de Dados", f"Informação: {dados}")
else:
    messagebox.showwarning("Atenção", "Nenhuma informação encontrada.")

# Execute o loop principal
root.mainloop()
'''
'''
from tkinter import Tk, Label
from PIL import Image, ImageTk

# Passo 1: Crie a janela Tkinter
janela = Tk()
janela.title("Janela com Imagem")

try:
    # Passo 2: Carregue a imagem usando Pillow
    imagem = Image.open("cristo.jpg")
    imagem_tk = ImageTk.PhotoImage(imagem)

    # Passo 3: Crie um widget Label e adicione a imagem
    label_imagem = Label(janela, image=imagem_tk)
    label_imagem.pack()

    # Passo 4: Inicie o loop principal da janela
    janela.mainloop()
except Exception as e:
    print(f"Erro ao carregar a imagem: {e}")
'''
'''
import tkinter as tk
from tkinter import PhotoImage

# Cria a janela principal
root = tk.Tk()

# Define o título da janela
root.title("Minha Janela")

# Carrega a imagem (certifique-se de que o caminho da imagem está correto)
icone = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")

# Define a imagem como ícone da janela
root.iconphoto(False, icone)

# Mantém a janela aberta
root.mainloop()
'''
from tkinter import *

# Janela principal
janela = Tk()
janela.geometry('1000x500')

janela.title("Imobiliária Garbin Craft")
icone = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")
janela.iconphoto(False, icone)

# Configurações de grid para centralizar
janela.grid_columnconfigure(0, weight=1)  # Configura a coluna 0 para ocupar o centro
janela.grid_rowconfigure(0, weight=1)    # Para centralizar verticalmente (opcional)

# Label Welcome
LabelWelcome = Label(janela, text="Seja bem-vindo à nossa imobiliária!", font=('Arial', 14, 'bold'))
LabelWelcome.grid(column=0, row=0, pady=10)

# Label Informacao
LabelInformacao = Label(janela, text="Precisamos de algumas informações antes de começar:", font=('Arial', 12, 'bold'))
LabelInformacao.grid(column=0, row=1)

# Mantém a janela aberta
janela.mainloop()
