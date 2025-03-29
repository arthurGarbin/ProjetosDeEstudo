from tkinter import *
from PIL import Image, ImageTk
from tkinter import PhotoImage

janela2 = Tk()
janela2.geometry('370x500')

janela2.title("Imobiliária Garbin Craft")

# Configurando o ícone
icone2_imagem = Image.open("C:/Users/Acer/Desktop/blocomine.png")
icone2 = ImageTk.PhotoImage(icone2_imagem)
janela2.iconphoto(False, icone2)

# Rótulo
rotulo = Label(janela2, text="Selecione o bioma que deseja ver", font=('Arial', 10, 'bold'))
rotulo.place(x=10, y=10)

# Imagem no botão
imagem = Image.open("C:/Users/Acer/Desktop/PlanVila.png")
imagem = imagem.resize((300, 100)) 
imagem_tk = ImageTk.PhotoImage(imagem)

ImagemRotulo = Label(janela2, image=imagem_tk)
ImagemRotulo.place(x=100, y=100)

janela2.mainloop()