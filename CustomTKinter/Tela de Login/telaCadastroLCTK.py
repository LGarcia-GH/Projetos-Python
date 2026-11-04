#region Bibliotecas Importadas  [ rgba(75,25,10)]
from importsLCTK import *
from registroLCTK import criarRegistro, salvarRegistro
from caminhosLCTK import *
#endregion


#region Locais de Arquivos
login_base = caminho_local()

caminho_icone = icone(login_base)

login, _, _, _, _, = scripts(login_base)
_, _, RSenha, _, _, = scripts(login_base)
_, _, _, logarADM, _ = scripts(login_base)
_, _, _, _, logarComum = scripts(login_base)
#endregion


#region Função de Registro JSON [ rgba(40,40,0)]
#Tenta Carregar o Arquivo Json com as Contas Registradas
contas = criarRegistro()
#endregion

#region Criação de Janela
#Cria uma nova Janela
janela = ctk.CTk()

#Função Para Usar Uma Imagem Como Icone do Programa
icone = tk.PhotoImage(file=caminho_icone)


#O comando iconephoto() é usado para definir o ícone da janela usando imagens ao invez de .ico
#AVISO: PODE SER USADO IMAGENS PNG, GIF, PPM/PGM, E PPM/PGM. NÃO FUNCIONA COM JPEG
janela.iconphoto(True, icone)

#Titulo da Janela do Programa
janela.title("Cadastro de Conta")
#Tamanho da Tela do Programa
janela.geometry("500x300")

janela.resizable(False, False)

#region Container dos Dados
registro = ctk.CTkFrame(janela)

registro.place(relx=0.40, rely=0.6, anchor="e")
#endregion

#region Container dos Botões
botoes = ctk.CTkFrame(janela)

botoes.place(relx=0.57, rely=0.6, anchor="w")
#endregion

#endregion


#region Texto Nome do Programa
titulo = ctk.CTkLabel(janela, text="PlaceHolder", font=("Roboto Mono", 16))
titulo.pack(pady=20)
#endregion

#region Aba de Email
#Texto de Login
emailJ = ctk.CTkLabel(registro, text="Email:", font=("Arial", 12))
emailJ.pack()

#Caixa de Texto de Email
email_entry = ctk.CTkEntry(registro)
email_entry.pack()
#endregion

#region Aba de Usuario
#Texto de Login
usuarioJ = ctk.CTkLabel(registro, text="Usuário:", font=("Arial", 12))
usuarioJ.pack()

#Caixa de Texto de Usuario
usuario_entry = ctk.CTkEntry(registro)
usuario_entry.pack()
#endregion

#region Aba de Senha
#Texto de Senha
senhaJ = ctk.CTkLabel(registro, text="Senha:", font=("Arial", 12))
senhaJ.pack()

#Caixa de Texto de Senha
senha_entry = ctk.CTkEntry(registro, show="*")
senha_entry.pack()
#endregion

#region Aba de Idade
idadeJ = ctk.CTkLabel(registro, text="Idade:", font=("Arial", 12))
idadeJ.pack()

#Caixa de Texto de Senha
idade_entry = ctk.CTkEntry(registro)
idade_entry.pack(pady=(0, 20))
#endregion

#region Botão de Tela de Login
#Função de Verificação de Login
def loginVerify():

    subprocess.Popen(["python3", login])
    sys.exit()

confirmar_button = ctk.CTkButton(botoes, text="Tela de Login", font=("Arial", 18), command=loginVerify)
confirmar_button.pack()
#endregion

#region Botão de Registrar
def conta_registrada():
    email = email_entry.get()
    usuario = usuario_entry.get().lower()
    senha = senha_entry.get()
    idade = int(idade_entry.get())

    if "@" not in email or ".com" not in email:
        messagebox.showerror("Erro","Esse E-mail Não é Valido")
    else:
        if email in contas["emailUsuario"]:
            messagebox.showerror("Erro","Essa conta já foi Registrada!!")
        else:
            contas["emailUsuario"][email] = usuario
            contas["senha"].append(senha)
            contas["idade"].append(idade)
            contas["superUsuario"].append(0)
            print(contas)

            salvarRegistro(contas)

            messagebox.showinfo("Sucesso", "Conta Registrada Com Sucesso!!!")

registrar = ctk.CTkButton(botoes, text="Cadastrar", font=("Arial", 18), command=conta_registrada)
registrar.pack()

#endregion

#Função de Loop do Programa (Mantem Ele Ativo Enquanto Aberto)
janela.mainloop()