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

        # O QHBoxLayout() Aplica os Layout de Forma Horizontal 
        # O QVBoxLayout() Aplica os Layout de Vertical
        # Neste Caso a Variavel janelaPrincipal Recebe Dois Layouts Dentro Dela Que Vão Ser Organizados de Forma Horizontal
        janelaPrincipal = QHBoxLayout()
        layout1 = QVBoxLayout()
        layout2 = QVBoxLayout()

        layout1.addWidget(Color('red'))
        layout1.addWidget(Color('yellow'))
        layout1.addWidget(Color('purple'))
        # setSpacing() Define o Espaçamento Interno do Widget.
        # setContentsMargins( ) Define a Margem do Widget
        layout1.setContentsMargins(0,0,0,0)
        layout1.setSpacing(20)

        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('purple'))

        janelaPrincipal.addLayout( layout1 )
        janelaPrincipal.addWidget(Color('green'))
        janelaPrincipal.addLayout( layout2 )


        widget = QWidget()
        widget.setLayout(janelaPrincipal)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
#endregion