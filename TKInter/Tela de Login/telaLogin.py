#region Bibliotecas Importadas  [ rgba(75,25,10)]
import tkinter as tk
from tkinter import messagebox
import subprocess
from registro import criarRegistro
from pathlib import Path
import sys
#endregion

#region Caminho Variavel
# Pega o diretório onde o arquivo atual (registro.py) está salvo
login_base = Path(__file__).resolve().parent

# Define o caminho completo usando a barra '/' para juntar as pastas
caminho_icone = login_base / "img" / "IconeF.png"
#endregion

#region Função de Registro JSON [ rgba(40,40,0)]
#Tenta Carregar o Arquivo Json com as Contas Registradas
contas = criarRegistro()
#endregion

#region Criação de Janela
#Cria uma nova Janela
janela = tk.Tk()

#Função Para Usar Uma Imagem Como Icone do Programa
icone = tk.PhotoImage(file=caminho_icone)

programa = tk.Frame(janela)

#O comando iconephoto() é usado para definir o ícone da janela usando imagens ao invez de .ico
#AVISO: PODE SER USADO IMAGENS PNG, GIF, PPM/PGM, E PPM/PGM. NÃO FUNCIONA COM JPEG
janela.iconphoto(True, icone)

#Titulo da Janela do Programa
janela.title("Login")
#Tamanho da Tela do Programa
janela.geometry("500x300")

programa.place(relx=0.5, rely=0.5, anchor="center")

janela.resizable(False, False)
#endregion


#region Texto Nome do Programa
titulo = tk.Label(programa, text="PlaceHolder", font=("Roboto Mono", 16))
titulo.pack(pady=(0,14))
#endregion


#region Aba de Login
#Texto de Login
usuarioJ = tk.Label(programa, text="Usuário:", font=("Arial", 12))
usuarioJ.pack()

#Caixa de Texto de Login
usuario_entry = tk.Entry(programa)
usuario_entry.pack()
#endregion

#region Aba de Senha
#Texto de Senha
SenhaJ = tk.Label(programa, text="Senha:", font=("Arial", 12))
SenhaJ.pack()

#Caixa de Texto de Senha
senha_entry = tk.Entry(programa, show="*")
senha_entry.pack(pady=(0, 10))
#endregion

#region Botão de Login
#Função de Verificação de Login
def loginVerify():
    usuario = usuario_entry.get().lower()
    senha = senha_entry.get()

    #Se o Usuario e Senha Estiverem Iguais ao Registro, o Login Ira Confirmar e Iniciar o Programa
    try:
        verificacao = list(contas["emailUsuario"].values())
        posicao = verificacao.index(usuario)
        print(posicao)

        #Se o Usuario e Senha Não Estiverem Iguais ao Registro, o Login Falhara
        if usuario in contas["emailUsuario"].values() and senha in contas["senha"]:
                if contas["superUsuario"][posicao] == 1:
                    subprocess.Popen(["python3", "usuarioADM.py"])
                    sys.exit()
                    print("Login do ADM Executado com Sucesso!")
                else: 
                    subprocess.Popen(["python3", "usuarioComum.py"])
                    sys.exit()
                    print("Login Executado com Sucesso!")
        else:
            raise ValueError()
    except (ValueError, KeyError):
        messagebox.showerror("Erro", "Usuario Não Existe no Sistema")
        print("Usuario Não Existe no Sistema")
        
    

    verificado = tk.Label(programa, text=" ")
    verificado.pack()

confirmar_button = tk.Button(programa, text="Logar", font=("Arial", 12), command=loginVerify)
confirmar_button.pack()
#endregion

#region Botão de Cadastrar
def telaCadastro():
    subprocess.Popen(["python3", "telaCadastro.py"])
    sys.exit()

registrar = tk.Button(programa, text="Cadastrar", font=("Arial", 12), command=telaCadastro)
registrar.pack()
#endregion

#region Botão de Recuperação de Senha
def telaRecuperar():
    subprocess.Popen(["python3", "telaSenha.py"])
    sys.exit()

recuperar = tk.Button(programa, text="Recuperar Senha", font=("Arial", 12), command=telaRecuperar)
recuperar.pack()
#endregion

#Função de Loop do Programa (Mantem Ele Ativo Enquanto Aberto)
janela.mainloop()