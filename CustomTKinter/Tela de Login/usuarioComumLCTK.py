#region Bibliotecas Importadas [ rgba(75,25,10)]
from importsLCTK import *
from registroLCTK import criarRegistro
from caminhosLCTK import *
#endregion


#region Locais de Arquivos
login_base = caminho_local()

caminho_icone = icone(login_base)

login, _, _, _, _, = scripts(login_base)
_, cadastrar, _, _, _, = scripts(login_base)
_, _, RSenha, _, _, = scripts(login_base)
_, _, _, logarADM, _ = scripts(login_base)

imagem, _, = imagens_login(login_base)
#endregion


#region Configuração Inicial do CustomTkinter
ctk.set_appearance_mode("dark")  # "System", "Dark", "Light"
ctk.set_default_color_theme("green")  # Tema padrão
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
janela.title("Janela do Usuario")
#Tamanho da Tela do Programa
janela.geometry("1000x700")

programa = ctk.CTkFrame(janela)
programa.place(relx=0.5, rely=0.5, anchor="center")
#endregion


#Imagem de Login

imgcomum = tk.PhotoImage(file=imagem)
comum = tk.Label(programa, image=imgcomum)
comum.pack(pady=20)

janela.mainloop()