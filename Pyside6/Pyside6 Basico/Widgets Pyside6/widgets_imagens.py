import sys
from pathlib import Path

from core_pyside6 import *

class Janela(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("App de Teste")

        #region Texto
        self.texto = QLabel("Gato")
        self.fonte = self.texto.font() # Cria uma variavel de vonte da varivavel de texto
        self.fonte.setPointSize(30) # Define o tamanho da fonte
        self.texto.setAlignment(
            Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter
        ) # Define o alinhamento do texto
        self.texto.setFont(self.fonte) # Define a fonte que o texto vai usar
        #endregion

        #region Imagem
        diretorio_atual = Path(__file__).resolve().parent # Caminho atual do arquivo
        caminho_imagem = diretorio_atual / "img" / "gato.png" # Caminho da imagem

        imagem = QLabel()
        imagem.setPixmap(QPixmap(caminho_imagem)) # Define o Label como imagem e pega o caminho da imagem
        imagem.setScaledContents(True) # Escala a imagem para a Janela
        #endregion

        #region Layout
        layout = QVBoxLayout()
        layout.addWidget(self.texto)
        layout.addWidget(imagem)
        #endregion

        #region Container
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        #endregion

app = QApplication(sys.argv)
window = Janela()
window.show()
app.exec()