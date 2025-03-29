#biblioteca
from tkinter import *

#criar janela/nome janela/tamanho janela
janela = Tk()
janela.title("Dados para teste")
janela.geometry('500x500')

#criar um rotulo/fonte(fonte n ta funcionando, testar mais tarde)/tamanho/cor/posição
Label = Label(janela, text="olá, Arthur", font = ('Arial Bold', 20), bg='Black', fg='White')
Label.grid(column=0, row=0)
#Label.pack()

#função para qnd apertar o botao abrir outra janela
def teste():
    janela2 = Tk()
    janela2.title("Bom dia")
    janela2.geometry('500x500')
    entrada = Entry(janela2, width=10)
    entrada.grid(column=0, row=0)
    bt_voltar = Button(janela2, text="Voltar", command=janela2.destroy)
    bt_voltar.grid(column=0, row=1)

#criar botao/tamannho/rodar funcao
botao = Button(janela, text="Clique", width='5', height='5', command=teste)
botao.place(x=250, y=250)

#janela fica aberta
janela.mainloop()