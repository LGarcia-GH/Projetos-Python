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

        self.setWindowTitle("Janela") # Define o título da janela

        self.caixa = QLineEdit() # Cria uma linha de texto na janela
        self.caixa.setPlaceholderText("Digite Algo") # Define o texto temporario da linha de texto

        self.botao = QPushButton("Aperte") # Cria um botão com texto
        # botao.setCheckable(True) # Define se vai ser um botão de alternancia ou não
        self.botao.clicked.connect(self.botao_clicado) # Executa a função selecionada dentro da propria classe
        # botao.clicked.connect(self.botao_clicou)

        self.setFixedSize(400, 300) # Define o tamanho da janela

        layout = QVBoxLayout() # Define uma variavel como ordem de layout
        layout.addWidget(self.caixa) # Define a ordem dos Widgets por linha de forma vertical
        layout.addWidget(self.botao)

        container = QWidget() # Container que vai receber todos os botões e desenhar tudo na janela
        container.setLayout(layout) # Define o layout da janela
        self.setCentralWidget(container) # Define a disposição do elementos na janela

        # self.setCentralWidget(self.botao) # Coloca o botão no centro da janela

       
    def botao_clicado(self):
        self.botao.setText("Apertou") # Define um texto a um texto ou botão
        print("Clicou!")

#    def botao_clicou(self, checked):
#        # checked é a varivale do Pyside6 que verifica se o botão está clicado ou não e retorna True ou False
#        print("Checado?", checked)

# Inicia a aplicação obrigatória do PySide6
app = QApplication(sys.argv)

# Cria uma instância da nossa janela personalizada
window = Janela_Principal() # Torna a janela visível na tela
window.show()

# Inicia o loop principal para manter o aplicativo rodando
app.exec()
