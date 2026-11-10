from pathlib import Path
from PIL import Image
from CTKImport import ctk

def caminho_local():
    caminho_base = Path(__file__).resolve().parent
    return caminho_base

def icone_local(caminho_base):
    caminho_icone = caminho_base/ "icon" / "Icone_Calculadora.png"
    return caminho_icone

#def fontes(login_base):
    #titulo = login_base / "fonts" / "BebasNeue-Regular.ttf"
    #return titulo

def teclas(login_base):

    backspace_caminho = login_base / "icon" / "teclas" / "backspace.png"
    backspace_covertido = Image.open(backspace_caminho)
    icone_backspace = ctk.CTkImage(light_image=backspace_covertido,
                                   dark_image=backspace_covertido,
                                   size=(24, 24))
    return icone_backspace