import sys  # Biblioteca do sistema para lidar com argumentos e fluxo do programa
from core_pyside6 import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("Widgets App")  # Define o título exibido na barra da janela

        layout = QVBoxLayout()  # Cria um gerenciador de layout vertical (empilha os itens de cima para baixo)
        widgets = [
            QCheckBox,       # Caixa de seleção (marcar/desmarcar)
            QComboBox,       # Menu suspenso (dropdown com opções)
            QDateEdit,       # Campo para exibir/editar datas
            QDateTimeEdit,   # Campo para exibir/editar data e hora juntas
            QDial,           # Botão giratório (medidor circular analógico)
            QDoubleSpinBox,  # Caixa de incremento/decremento para números decimais
            QFontComboBox,   # Menu suspenso para seleção de fontes de texto
            QLCDNumber,      # Display numérico estilo tela de LCD
            QLabel,          # Rótulo simples para exibir textos ou imagens
            QLineEdit,       # Campo de entrada de texto de linha única
            QProgressBar,    # Barra de progresso (indica carregamento)
            QPushButton,     # Botão clicável tradicional
            QRadioButton,    # Botão de rádio (escolha exclusiva em um grupo)
            QSlider,         # Controle deslizante horizontal ou vertical
            QSpinBox,        # Caixa de incremento/decremento para números inteiros
            QTimeEdit,       # Campo para exibir/editar horários
        ]

        for widget in widgets:
            layout.addWidget(widget())  # Instancia cada widget da lista e adiciona ao layout vertical

        central_widget = QWidget()  # Cria um widget genérico para servir de container central
        central_widget.setLayout(layout)  # Aplica o layout vertical dentro do container central

        self.setCentralWidget(central_widget)  # Define o container como a área central da janela principal

app = QApplication(sys.argv)  # Inicializa o gerenciador da aplicação GUI
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6')) # Aplicar tema escuro no pyside

window = MainWindow()  # Cria uma instância da janela principal da aplicação
window.show()  # Torna a janela visível na tela

app.exec()  # Inicia o loop de eventos da aplicação (mantém a janela rodando e interativa)