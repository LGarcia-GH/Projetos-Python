#region Imports
from core_pyside6 import *
from layoutcolor import Color
import sys
#endregion


#region Janela Principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        # Define o Layout da Variavel em Forma de Camadas
        layout = QStackedLayout()


        Cor1 = Color('red')
        Cor2 = Color('green')
        Cor3 = Color('blue')
        Cor4 = Color('yellow')

        layout.addWidget(Cor1)
        layout.addWidget(Cor2)
        layout.addWidget(Cor3)
        layout.addWidget(Cor4)

        # Usando Index Para Definir a Prioridade
       #layout.setCurrentIndex(3)

        # Usando Variaveis Para Definir a Prioridade
        layout.setCurrentWidget(Cor2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
#endregion