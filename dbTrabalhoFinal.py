from tkinter import *
from tkinter import messagebox
import sqlite3


#connectar ao banco de dados
conn = sqlite3.connect('DBpy.db')
cursor = conn.cursor()


#função para adicionar item
def add_item(nome, qnt, cod):
    cursor.execute('''INSERT INTO produtos (produto, quantidade, codigo) VALUES (?, ?, ?)''', (nome, qnt, cod))
    messagebox.showinfo("","Seu item já foi adicionado no banco de dados")
    conn.commit()
#função para criar a janela de adicionar
def janela_add():
    janela2 = Tk()
    janela2.title("Dados")
    janela2.geometry('500x500')

    label_nome = Label(janela2, text="Coloque o nome do item: ")
    label_nome.grid(column=0, row=0)
    nome = Entry(janela2, width=10)
    nome.grid(column=1, row=0)

    label_qnt = Label(janela2, text="Coloque quantos itens são: ")
    label_qnt.grid(column=0, row=1)
    qnt = Entry(janela2, width=10)
    qnt.grid(column=1, row=1)

    label_cod = Label(janela2, text="Coloque o código do item: ")
    label_cod.grid(column=0, row=2)
    cod = Entry(janela2, width=10)
    cod.grid(column=1, row=2)

    def on_confirm():
        add_item(nome.get(), qnt.get(), cod.get())

    bt_confirmar = Button(janela2, text="Adicionar item", command=on_confirm)
    bt_confirmar.grid(column=0, row=3)

    bt_voltar = Button(janela2, text="Voltar", command=janela2.destroy)
    bt_voltar.grid(column=0, row=4)

#função informar sobre algum item(em trabalho)
def informar():
    inform = Tk()
    inform.title("Informações")
    inform.geometry('500x500')

#função para editar algum item (em trabalho)
def editar():
    edit = Tk()
    edit.title("Editar")
    edit.geometry('500x500')

#função para remover
def remocao(entrada_remov):
    cursor.execute('''DELETE FROM produtos WHERE id = ?''', (entrada_remov))
    messagebox.showinfo("","Seu item foi removido do banco de dados")
    conn.commit()
#função criar janela para remover algum item
def remover():
    remov = Tk()
    remov.title("Remover")
    remov.geometry('500x500')

    text_remov = Label(remov, text="Digite a ID do item que deseja remover: ")
    text_remov.grid(column=0, row=0)

    entrada_remov = Entry(remov, width=10)
    entrada_remov.grid(column=1, row=0)

    def confirm():
        remocao(entrada_remov.get())

    bt_confirmar = Button(remov, text="Confirmar", command=confirm)
    bt_confirmar.grid(column=0, row=1)

    bt_voltar = Button(remov, text="Voltar", command=remov.destroy)
    bt_voltar.grid(column=0, row=2)

#janela principal
janela = Tk()
janela.title("Banco de dados")
janela.geometry('500x600')

txt_inicio = Label(janela, text="Olá, o que deseja fazer?", width=25, height=5, font=('Arial', 10))
txt_inicio.grid(column=0, row=0)

bt_add = Button(janela, text="Adicione um item", width=25, height=5, font=('Arial', 10), command=janela_add)
bt_add.grid(column=0, row=1)

bt_select = Button(janela, text="Informações de algum item", width=25, height=5, font=('Arial', 10), command=informar)
bt_select.grid(column=0, row=2)

bt_editar = Button(janela, text="Edite algum item", width=25, height=5, font=('Arial', 10), command=editar)
bt_editar.grid(column=0, row=3)

bt_remove = Button(janela, text="Remova algum item", width=25, height=5, font=('Arial', 10), command=remover)
bt_remove.grid(column=0, row=4)

bt_fechar = Button(janela, text="Sair", width=25, height=5, font=('Arial', 10), command=janela.destroy)
bt_fechar.grid(column=0, row=5)

janela.mainloop()