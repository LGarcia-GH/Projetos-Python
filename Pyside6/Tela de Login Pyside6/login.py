#region Bibliotecas importadas [rgb (0, 0, 50)]
import sys
import subprocess

from core_pyside6 import *
from PySide6.QtCore import Qt
#endregion


class Janela_Principal(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tela de Login")
        self.setMaximumSize(700, 500)
        self.setMinimumSize(500, 300)

        self.telaPrincipal = QStackedLayout()

        #region Tela de Login
        self.telaLoginLayout = QWidget()

        # Layout vertical principal para centralizar tudo no meio do ecrã (vertical e horizontal)
        layout_principal_login = QVBoxLayout(self.telaLoginLayout)
        layout_principal_login.addStretch()

        # Contentor do formulário para manter os elementos juntos e organizados
        container_form = QWidget()
        form_layout = QVBoxLayout(container_form)
        form_layout.setSpacing(10)  # Espaçamento vertical entre os elementos

        # 1. Linha do Utilizador (Rótulo + Caixa de texto lado a lado)
        linha_usuario = QHBoxLayout()
        self.tusuario = QLabel("Usuario:")
        self.tusuario.setFixedWidth(60)  # Largura fixa para alinhar os rótulos
        self.usuario_entry = QLineEdit()
        self.usuario_entry.setPlaceholderText("Digite o Usuario")
        self.usuario_entry.setFixedSize(220, 30)
        linha_usuario.addWidget(self.tusuario)
        linha_usuario.addWidget(self.usuario_entry)

        # 2. Linha da Senha (Rótulo + Caixa de texto lado a lado)
        linha_senha = QHBoxLayout()
        self.tsenha = QLabel("Senha:")
        self.tsenha.setFixedWidth(60)  # Mesma largura do rótulo anterior para alinhar perfeitamente
        self.senha_entry = QLineEdit()
        self.senha_entry.setPlaceholderText("Digite a Senha") 
        self.senha_entry.setFixedSize(220, 30)
        self.senha_entry.setEchoMode(QLineEdit.EchoMode.Password)
        linha_senha.addWidget(self.tsenha)
        linha_senha.addWidget(self.senha_entry)

        # 3. Linha dos Botões de Ação (Logar e Cadastrar lado a lado)
        linha_botoes = QHBoxLayout()
        self.logar = QPushButton("Logar")
        self.logar.setFixedSize(105, 35)

        self.cadastrar = QPushButton("Cadastrar")
        self.cadastrar.setFixedSize(105, 35)
        
        linha_botoes.addWidget(self.logar)
        linha_botoes.addWidget(self.cadastrar)

        # 4. Botão de Recuperar Senha (com a mesma largura total dos campos de cima)
        self.recuperar_senha = QPushButton("Recuperar Senha")
        self.recuperar_senha.setFixedSize(220, 35)

        # Adicionar todas as linhas estruturadas ao layout do formulário
        form_layout.addLayout(linha_usuario)
        form_layout.addLayout(linha_senha)
        form_layout.addLayout(linha_botoes)
        form_layout.addWidget(self.recuperar_senha, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adicionar o formulário completo e centralizado no layout principal da janela
        layout_principal_login.addWidget(container_form, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_principal_login.addStretch()
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

        container = QWidget()
        container.setLayout(self.telaPrincipal)
        self.setCentralWidget(container)


app = QApplication(sys.argv)
window = Janela_Principal()
window.show()
app.exec()