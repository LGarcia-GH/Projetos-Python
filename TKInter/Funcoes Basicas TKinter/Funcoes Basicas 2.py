from tkinter import *
from tkinter import ttk, simpledialog

texto = str()

#Variavel da biblioteca TK
programa = Tk()

#Titulo da Janela
programa.title("Teste")

#Define o Tamanho Inicial da Janela (Largura x Altura)
programa.geometry("400x300")

#Comando para criar um container com as funções e botões que vc criar
# AVISO: O PARAMETRO PADDING SERVE PARA DECIDIR O ESPAÇAMENTO INTERNO DO CONTAINER
principal = ttk.Frame(programa, padding=10)

#Comando para organizar os containers em forma de grid na janela
principal.grid()

#Serve para Ocultar uma Janela
programa.withdraw()


#Comando para Criar uma tela de Digitação Para o Usuario, Onde vc pode Coletar Dados
digite = simpledialog.askstring("Teste", "Escreva aqui: ")

#Usando o comando print na variavel botão com as propriedades .configure() e .keys, mostram as ações
#possiveis com aquele botão
#print(botao.configure().keys())
if digite:
    print("Funcionou")
    texto = digite


#O Comando .deiconify() para Mostrar a Janela Novamente
programa.deiconify()

#Comando para Escrever Textos na Janela
world = ttk.Label(principal, text=texto)
world.grid(column=0, row=0)

#Comando para Criar um Botão (a linha .destroy serve para fechar a janela)
botao = ttk.Button(principal, text="Fechar", command=programa.destroy)

botao.grid(column=1, row=0)


programa.mainloop()