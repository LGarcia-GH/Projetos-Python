#region Bibliotecas Importadas  [ rgba(75,25,10)]
import tkinter as tk
from tkinter import messagebox
import subprocess
from registro import criarRegistro
import sys
#endregion

#region Função de Registro JSON [ rgba(40,40,0)]
#Tenta Carregar o Arquivo Json com as Contas Registradas
contas = criarRegistro()
#endregion

#region Criação de Janela
#Cria uma nova Janela
janela = tk.Tk()

#Função Para Usar Uma Imagem Como Icone do Programa
icone = tk.PhotoImage(file="img/IconeF.png")

programa = tk.Frame(janela)
programa.place(relx=0.5, rely=0.5, anchor="center")

#O comando iconephoto() é usado para definir o ícone da janela usando imagens ao invez de .ico
#AVISO: PODE SER USADO IMAGENS PNG, GIF, PPM/PGM, E PPM/PGM. NÃO FUNCIONA COM JPEG
janela.iconphoto(True, icone)

#Titulo da Janela do Programa
janela.title("Recuperação de Senha")
#Tamanho da Tela do Programa
janela.geometry("500x300")

janela.resizable(False, False)
#endregion


#region Texto Nome do Programa
titulo = tk.Label(programa, text="PlaceHolder", font=("Roboto Mono", 16))
titulo.pack(pady=(0,18))
#endregion


#region Aba de Verificação de Email
#Texto de Login
emailJ = tk.Label(programa, text="Email:", font=("Arial", 12))
emailJ.pack()

#Caixa de Texto de Verificação de Email
email_entry = tk.Entry(programa)
email_entry.pack()
#endregion

#region Aba de Verificação de Idade
idadeJ = tk.Label(programa, text="Idade:", font=("Arial", 12))
idadeJ.pack()

#Caixa de Texto de Verificação de Email
idade_entry = tk.Entry(programa)
idade_entry.pack()
#endregion

#region Botão de Recuperar Senha
#Função de Verificação de Login
def loginVerify():
    email = email_entry.get()
    idade = int(idade_entry.get())

    #Se o Email Estiver Correto e Idade Estiverem Corretos
    try:
        verificacao = list(contas["emailUsuario"].keys())
        posicao = verificacao.index(email)
        print(posicao)
        senha = str()
        if email in contas["emailUsuario"] and idade == contas["idade"][posicao]:
            senha = contas["senha"][posicao]
            print(senha)
            messagebox.showinfo("Senha Recuperada", f"{senha}")
        else:
            raise ValueError()
 
    except (ValueError, KeyError):
        messagebox.showerror("Erro", "Usuario Não Existe no Sistema")
        print("Usuario Não Existe no Sistema")
        

confirmar_button = tk.Button(programa, text="Recuperar", font=("Arial", 18), command=loginVerify)
confirmar_button.pack(pady=(10,0))
#endregion

#region Botão de Tela de Login
#Função de Verificação de Login
def loginVerify():

    subprocess.Popen(["python3", "telaLogin.py"])
    sys.exit()

confirmar_button = tk.Button(programa, text="Tela de Login", font=("Arial", 18), command=loginVerify)
confirmar_button.pack()
#endregion

#Função de Loop do Programa (Mantem Ele Ativo Enquanto Aberto)
janela.mainloop()