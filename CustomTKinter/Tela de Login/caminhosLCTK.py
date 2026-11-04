from pathlib import Path

def caminho_local():
    login_base = Path(__file__).resolve().parent
    return login_base

def icone(login_base):
    caminho_icone = login_base / "img" / "IconeF.png"
    return caminho_icone

def scripts(login_base):
    caminho_login = login_base / "telaLoginLCTK.py"
    caminho_cadastro = login_base / "telaCadastroLCTK.py"
    caminho_RSenha = login_base / "telaRSenhaLCTK.py"

    caminho_usuarioADM = login_base / "usuarioADMLCTK.py"
    caminho_usuarioComum = login_base / "usuarioComumLCTK.py"
    return caminho_login, caminho_cadastro, caminho_RSenha, caminho_usuarioADM, caminho_usuarioComum

def imagens_login(login_base):
    imagem_usuario_comum = login_base / "img" / "usuario.png"
    imagem_usuario_adm = login_base / "img" / "Adm.png"
    return imagem_usuario_comum, imagem_usuario_adm
