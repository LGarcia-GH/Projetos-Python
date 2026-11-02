from core_pyside6 import QColor, QPalette, QWidget


# Classe 'Color' herdando de QWidget (a base para qualquer componente visual no PySide6)
class Color(QWidget):
    def __init__(self, color):
        super().__init__()

        # Diz ao Qt para preencher o fundo automaticamente com a cor da paleta
        self.setAutoFillBackground(True)
        # Pega a paleta de cores atual do widget
        palette = self.palette()
        # Altera a cor da "Janela" (o fundo do widget) para a cor que você passou como parâmetro
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        # Aplica essa nova paleta modificada de volta ao widget
        self.setPalette(palette)