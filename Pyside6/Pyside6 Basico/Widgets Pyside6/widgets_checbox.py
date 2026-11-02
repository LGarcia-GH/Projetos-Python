import sys  # Biblioteca do sistema para lidar com argumentos e fluxo do programa
from core_pyside6 import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__() 

        self.setWindowTitle("Check Box")
        
        checkbox = QCheckBox("Uma Caixa")
        checkbox.setCheckState(Qt.CheckState.Checked)
        checkbox.stateChanged.connect(self.show_state) # Verifica a mudança de checagem e chama a função show_state

        selecao = QComboBox()
        selecao.addItems(["Um", "Dois", "Três", "Quatro"])

        layout = QVBoxLayout()
        layout.addWidget(checkbox)
        layout.addWidget(selecao)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
    
    def show_state(self, state):
        print(state == Qt.CheckState.Checked.value)
        print(state)

app = QApplication(sys.argv)  # Inicializa o gerenciador da aplicação GUI
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyside6')) # Aplicar tema escuro no pyside

window = MainWindow()  # Cria uma instância da janela principal da aplicação
window.show()  # Torna a janela visível na tela

app.exec()  # Inicia o loop de eventos da aplicação (mantém a janela rodando e interativa)