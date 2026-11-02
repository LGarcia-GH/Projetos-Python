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

        self.tusuario = QLabel("Usuario") # Cria um texto na janela
        self.usuario_entry = QLineEdit() # Cria uma linha de texto na janela
        self.usuario_entry.setPlaceholderText("Digite o Usuario") # Define o texto temporario da linha de texto

        self.tsenha = QLabel("Senha")
        self.senha_entry = QLineEdit()
        self.senha_entry.setPlaceholderText("Digite a Senha")

        self.logar = QPushButton("Logar") # Cria um botão com texto
        self.logar.clicked.connect(self.botao_clicado) # Executa a função selecionada dentro da propria classe

        self.cadastrar = QPushButton("Cadastrar")

        self.recuperar_senha = QPushButton("Recuperar Senha")

        self.setFixedSize(500, 300) # Define o tamanho da janela

        layout = QVBoxLayout() # Define uma variavel como ordem de layout
        layout.addWidget(self.tusuario) # Define a ordem dos Widgets por linha de forma vertical
        layout.addWidget(self.usuario_entry)
        layout.addWidget(self.tsenha)
        layout.addWidget(self.senha_entry)
        layout.addWidget(self.logar)
        layout.addWidget(self.cadastrar)
        layout.addWidget(self.recuperar_senha)

        container = QWidget() # Container que vai receber todos os botões e desenhar tudo na janela
        container.setLayout(layout) # Define o layout da janela
        self.setCentralWidget(container) # Define a disposição do elementos na janela

       
    def botao_clicado(self):
        self.botao.setText("Apertou") # Define um texto a um texto ou botão
        print("Clicou!")


# Inicia a aplicação obrigatória do PySide6
app = QApplication(sys.argv)

# Cria uma instância da nossa janela personalizada
window = Janela_Principal() # Torna a janela visível na tela
window.show()

# Inicia o loop principal para manter o aplicativo rodando
app.exec()