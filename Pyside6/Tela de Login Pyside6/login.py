#region Bibliotecas importadas [rgb (0, 0, 50)]
import sys
import subprocess

from core_pyside6 import *
#endregion


# Uma classe de janela personalizada herdando de QMainWindow
class Janela_Principal(QMainWindow):
    # O __init__ inicia o comando dentro da função assim que o codigo inicia
    def __init__(self):
        super().__init__() # Inicializa a codigo que a classe está erdando

        self.setWindowTitle("Tela de Login") # Define o título da janela

        self.telaPrincipal = QStackedLayout()

        #region Tela de Login
        self.telaLoginLayout = QWidget()

        self.tusuario = QLabel("Usuario") # Cria um texto na janela
        self.usuario_entry = QLineEdit() # Cria uma linha de texto na janela
        self.usuario_entry.setPlaceholderText("Digite o Usuario") # Define o texto temporario dentro da linha de texto

        self.tsenha = QLabel("Senha")
        self.senha_entry = QLineEdit()
        self.senha_entry.setPlaceholderText("Digite a Senha") 

        self.logar = QPushButton("Logar") # Cria um botão com texto

        self.cadastrar = QPushButton("Cadastrar")

        self.recuperar_senha = QPushButton("Recuperar Senha")

        self.setFixedSize(500, 300) # Define o tamanho da janela

        gridTelaLogin = QVBoxLayout()
        gridTelaLogin.addWidget(self.tusuario) # Define a ordem dos Widgets por linha de forma vertical
        gridTelaLogin.addWidget(self.usuario_entry)
        gridTelaLogin.addWidget(self.tsenha)
        gridTelaLogin.addWidget(self.senha_entry)
        gridTelaLogin.addWidget(self.logar)
        gridTelaLogin.addWidget(self.cadastrar)
        gridTelaLogin.addWidget(self.recuperar_senha)

        telaLogin = QGridLayout() # Define uma variavel como ordem de layout de diferentes aspectos
        telaLogin.addLayout(gridTelaLogin, 0, 1)

        self.telaLoginLayout.setLayout(telaLogin) # Guarda tudo dentro de um container QWidget()
        #endregion

        #region Tela de Cadastro
        self.telaCadastroLayout = QWidget()


        #endregion

        #region Tela de Recuperação de Senha
        self.telaRecuperarSenha = QWidget()


        #endregion

        self.telaPrincipal.addWidget(self.telaLoginLayout)
        self.telaPrincipal.addWidget(self.telaCadastroLayout)
        self.telaPrincipal.addWidget(self.telaRecuperarSenha)
        self.telaPrincipal.setCurrentWidget(self.telaLoginLayout)

        container = QWidget() # Container que vai receber todos os botões e desenhar tudo na janela
        container.setLayout(self.telaPrincipal) # Define o layout da janela
        self.setCentralWidget(container) # Define a disposição do elementos na janela


# Inicia a aplicação obrigatória do PySide6
app = QApplication(sys.argv)

# Cria uma instância da nossa janela personalizada
window = Janela_Principal() # Torna a janela visível na tela
window.show()

# Inicia o loop principal para manter o aplicativo rodando
app.exec()