#region Bibliotecas Importadas  [ rgba(75,25,10)]
from importsLCTK import *
from registroLCTK import criarRegistro
from caminhosLCTK import *
#endregion

#region Locais de Arquivos
login_base = caminho_local()

caminho_icone = icone(login_base)

titulo = fontes(login_base)

_, cadastrar, _, _, _, = scripts(login_base)
_, _, RSenha, _, _, = scripts(login_base)
_, _, _, logarADM, _ = scripts(login_base)
_, _, _, _, logarComum = scripts(login_base)
#endregion


#region Configuração Inicial do CustomTkinter
ctk.set_appearance_mode("dark")  # "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Tema padrão
#endregion


#region Função de Registro JSON [ rgba(40,40,0)]
# Tenta Carregar o Arquivo Json com as Contas Registradas
contas = criarRegistro()
#endregion


#region Criação de Janela
# Cria uma nova Janela usando CTk
janela = ctk.CTk()

icone = tk.PhotoImage(file=caminho_icone)
janela.iconphoto(True, icone)

programa = ctk.CTkFrame(janela, fg_color="transparent")

# Titulo da Janela do Programa
janela.title("Login")
# Tamanho da Tela do Programa
janela.geometry("700x400")

programa.place(relx=0.5, rely=0.5, anchor="center")

janela.resizable(False, False)
#endregion


#region Texto Nome do Programa
titulo = ctk.CTkLabel(programa, text="PlaceHolder", font=(titulo, 30))
titulo.pack(pady=(0, 40))
#endregion


#region Aba de Login
# Texto de Login
usuarioJ = ctk.CTkLabel(programa, text="Usuário:", font=("Arial", 18))
usuarioJ.pack()

# Caixa de Texto de Login
usuario_entry = ctk.CTkEntry(programa)
usuario_entry.pack()
#endregion

#region Aba de Senha
# Texto de Senha
SenhaJ = ctk.CTkLabel(programa, text="Senha:", font=("Arial", 18))
SenhaJ.pack()

# Caixa de Texto de Senha
senha_entry = ctk.CTkEntry(programa, show="*")
senha_entry.pack(pady=(0, 10))
#endregion

#region Botão de Login
# Função de Verificação de Login
def loginVerify():
    usuario = usuario_entry.get().lower()
    senha = senha_entry.get()

    # Se o Usuario e Senha Estiverem Iguais ao Registro, o Login Ira Confirmar e Iniciar o Programa
    try:
        verificacao = list(contas["emailUsuario"].values())
        posicao = verificacao.index(usuario)
        print(posicao)

        # Se o Usuario e Senha Não Estiverem Iguais ao Registro, o Login Falhara
        if usuario in contas["emailUsuario"].values() and senha in contas["senha"]:
                if contas["superUsuario"][posicao] == 1:
                    subprocess.Popen(["python3", logarADM])
                    sys.exit()
                    print("Login do ADM Executado com Sucesso!")
                else: 
                    subprocess.Popen(["python3", logarComum])
                    sys.exit()
                    print("Login Executado com Sucesso!")
        else:
            raise ValueError()
    except (ValueError, KeyError):
        messagebox.showerror("Erro", "Usuario Não Existe no Sistema")
        print("Usuario Não Existe no Sistema")

confirmar_button = ctk.CTkButton(programa, text="Logar", font=("Arial", 16), command=loginVerify)
confirmar_button.pack(pady=5)
#endregion

#region Botão de Cadastrar
def telaCadastro():
    subprocess.Popen(["python3", cadastrar])
    sys.exit()

registrar = ctk.CTkButton(programa, text="Cadastrar", font=("Arial", 16), command=telaCadastro)
registrar.pack(pady=5)
#endregion

#region Botão de Recuperação de Senha
def telaRecuperar():
    subprocess.Popen(["python3", RSenha])
    sys.exit()

recuperar = ctk.CTkButton(programa, text="Recuperar Senha", font=("Arial", 16), command=telaRecuperar)
recuperar.pack(pady=5)
#endregion

# Função de Loop do Programa (Mantem Ele Ativo Enquanto Aberto)
janela.mainloop()