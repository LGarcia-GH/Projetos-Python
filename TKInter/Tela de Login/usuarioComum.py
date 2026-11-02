#region Bibliotecas Importadas [ rgba(75,25,10)]
import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import sys
#endregion

#region Criação de Janela
#Cria uma nova Janela
janela = tk.Tk()

#Função Para Usar Uma Imagem Como Icone do Programa
icone = tk.PhotoImage(file="img/IconeF.png")

#O comando iconephoto() é usado para definir o ícone da janela usando imagens ao invez de .ico
#AVISO: PODE SER USADO IMAGENS PNG, GIF, PPM/PGM, E PPM/PGM. NÃO FUNCIONA COM JPEG
janela.iconphoto(True, icone)

#Titulo da Janela do Programa
janela.title("Janela do Usuario")
#Tamanho da Tela do Programa
janela.geometry("1000x700")

programa = tk.Frame(janela)
programa.place(relx=0.5, rely=0.5, anchor="center")
#endregion


#Imagem de Login

imgcomum = tk.PhotoImage(file="img/usuario.png")
comum = tk.Label(programa, image=imgcomum)
comum.pack(pady=20)

janela.mainloop()