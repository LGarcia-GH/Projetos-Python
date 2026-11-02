from tkinter import *
from tkinter import ttk, simpledialog


#Variavel da biblioteca TK
programa = Tk()

#O funcao tk.PhotoImage() é usada para carregar uma imagem
icone = tk.PhotoImage(file="./img/ico/iconeF.png")

#O comando iconephoto() é usado para definir o ícone da janela usando imagens ao invez de .ico
#AVISO: PODE SER USADO IMAGENS PNG, GIF, PPM/PGM, E PPM/PGM. NÃO FUNCIONA COM JPEG
programa.iconphoto(True, icone)

#Titulo da Janela
programa.title("Teste")

#Define o Tamanho Inicial da Janela (Largura x Altura)
programa.geometry("400x300")


#Comando para criar um container com as funções e botões que vc criar
# AVISO: O PARAMETRO PADDING SERVE PARA DECIDIR O ESPAÇAMENTO INTERNO DO CONTAINER
principal = ttk.Frame(programa, padding=10)

#Comando para empilhar e alinhar os containers sequencialmente na janela (em blocos topo, base, esquerda ou direita)
principal.pack()


#Comando para Escrever Textos na Janela
escrito = ttk.Label(principal, text="Digite Algo")
escrito.pack()


escrever = ttk.Entry(principal)
escrever.pack()

def botao_clicado():
    texto = escrever.get()
    escrito["text"] = texto

#Comando para Criar um Botão (a linha .destroy serve para fechar a janela)
botao = ttk.Button(principal, text="Confirmar", command=botao_clicado)
botao.pack()


#Comando para Criar uma tela de Digitação Para o Usuario.
programa.mainloop()