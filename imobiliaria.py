from tkinter import *
from tkinter import PhotoImage
from PIL import Image, ImageTk
import sqlite3

#connectar ao banco de dados
conn = sqlite3.connect('imobiliaria.db')
cursor = conn.cursor()

#Tela login
def login():
    entrada.destroy()

    telaLogin = Tk()
    telaLogin.geometry('370x500')

    telaLogin.title("Login")
    icone = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")
    telaLogin.iconphoto(False, icone)

    loginLabel = Label(telaLogin, text="Por favor, entre com seu email e CPF:", font=('Arial', 10, 'bold'))
    loginLabel.grid(column=0, row=0)

    loginEmail = Label(telaLogin, text="Email: ", font=('Arial', 10, 'bold'))
    loginEmail.place(x=10, y=60)
    EntradaLoginEmail = Entry(telaLogin, width=35)
    EntradaLoginEmail.place(x=70, y=62.5)

    LabelCpf = Label(telaLogin, text="CPF: ", font=('Arial', 10, 'bold'))
    LabelCpf.place(x=10, y=100)
    EntradaCpf = Entry(telaLogin, width=35)
    EntradaCpf.place(x=70, y=102.5)

    def continuar():
        telaLogin.destroy()

        janela2 = Tk()
        janela2.geometry('370x500')

        janela2.title("Imobiliária Garbin Craft")
        icone2 = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")
        janela2.iconphoto(False, icone2)

        janela2.mainloop

    BtContinuar = Button(telaLogin, text="Continuar", width=9, height=2, font=('Arial', 10, 'bold'), command=continuar)
    BtContinuar.place(x=10, y=150)

    BtSair = Button(telaLogin, text="Sair", width=9, height=2, font=('Arial', 10, 'bold'), command=telaLogin.destroy)
    BtSair.place(x=115, y=150)

    imagem = Image.open("C:/Users/Acer/Desktop/certo31.png")
    imagem = imagem.resize((300, 100)) 
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = Label(telaLogin, image=imagem_tk)
    label_imagem.place(x=5, y=200)

    telaLogin.mainloop()

#Tela cadastro
def cadastro():
    entrada.destroy()

    janela = Tk()
    janela.geometry('370x500')

    janela.title("Cadastro")
    icone = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")
    janela.iconphoto(False, icone)

    LabelWelcome = Label(janela, text="Seja bem vindo a nossa imobiliária!", font=('Arial', 10, 'bold'))
    LabelWelcome.grid(column=0, row=0)

    LabelInformacao = Label(janela, text="Precisamos de algumas informações antes de começar:", font=('Arial', 10, 'bold'))
    LabelInformacao.grid(column=0, row=1)

    LabelNome = Label(janela, text="Nome: ", font=('Arial', 10, 'bold'))
    LabelNome.place(x=10, y=60)
    EntradaNome = Entry(janela, width=35)
    EntradaNome.place(x=110, y=62.5)

    LabelEmail = Label(janela, text="Email: ", font=('Arial', 10, 'bold'))
    LabelEmail.place(x=10, y=100)
    EntradaEmail = Entry(janela, width=35)
    EntradaEmail.place(x=110, y=102.5)

    LabelNumero = Label(janela, text="Número (DDD): ", font=('Arial', 10, 'bold'))
    LabelNumero.place(x=10, y=140)
    EntradaNumero = Entry(janela, width=35)
    EntradaNumero.place(x=110, y=142.5)

    LabelCPF = Label(janela, text="CPF: ", font=('Arial', 10, 'bold'))
    LabelCPF.place(x=10, y=180)
    EntradaCPF = Entry(janela, width=35)
    EntradaCPF.place(x=110, y=182.5)

    def continuar():
        janela.destroy()

        janela2 = Tk()
        janela2.geometry('370x500')

        janela2.title("Imobiliária Garbin Craft")
        icone2 = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")
        janela2.iconphoto(False, icone2)

        janela2.mainloop

    BtContinuar = Button(janela, text="Continuar", width=9, height=2, font=('Arial', 10, 'bold'), command=continuar)
    BtContinuar.place(x=10, y=250)

    BtSair = Button(janela, text="Sair", width=9, height=2, font=('Arial', 10, 'bold'), command=janela.destroy)
    BtSair.place(x=115, y=250)

    imagem = Image.open("C:/Users/Acer/Desktop/certo31.png")
    imagem = imagem.resize((300, 100)) 
    imagem_tk = ImageTk.PhotoImage(imagem)

    label_imagem = Label(janela, image=imagem_tk)
    label_imagem.place(x=5, y=300)

    janela.mainloop()

#janela cadastro
entrada = Tk()
entrada.geometry('370x500')

entrada.title("Login/Cadastro")
icone = PhotoImage(file="C:/Users/Acer/Desktop/blocomine.png")
entrada.iconphoto(False, icone)

imagem = Image.open("C:/Users/Acer/Desktop/certo31.png")
imagem = imagem.resize((300, 100)) 
imagem_tk = ImageTk.PhotoImage(imagem)

lb_imagem = Label(entrada, image=imagem_tk)
lb_imagem.place(x=50, y=10)

labelEntrada = Label(entrada, text="Por favor, faça o cadastro ou entre com seu login", font=('Arial', 10, 'bold'))
labelEntrada.place(x=25, y=100)

btLogin = Button(entrada, text="Login", width=10, height=3, font=('Arial', 10, 'bold'), command=login)
btLogin.place(x=125, y=170)

btCadastro = Button(entrada, text="Cadastro", width=10, height=3, font=('Arial', 10, 'bold'), command=cadastro)
btCadastro.place(x=125, y=250)

btSair = Button(entrada, text="Sair", width=10, height=3, font=('Arial', 10, 'bold'), command=entrada.destroy)
btSair.place(x=125, y=400)

entrada.mainloop()