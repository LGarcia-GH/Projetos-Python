from CTKImport import *
# Biblioteca Usada Para Receber Textox String e Converte-los Para Operações Matemáticas
import sympy as sp


#region Criação da Janela do CustomTKinter
ctk.set_appearance_mode("dark")  # "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Tema padrão

janela = ctk.CTk()
programa = ctk.CTkFrame(janela, fg_color="transparent")
janela.title("Calculadora")
janela.geometry("320x500")
programa.place(relx=0.5, rely=0.5, anchor="center")
janela.resizable(False, False)
#endregion Criação da Janela do CustomTKinter

#region Container de Botões
linha0 = ctk.CTkFrame(programa)
linha1 = ctk.CTkFrame(programa)
linha2 = ctk.CTkFrame(programa)
linha3 = ctk.CTkFrame(programa)
edit = ctk.CTkFrame(programa)
#endregion

#region Funções da Caixa de Texto

# É Definida Uma Variavel TKinter, Necessario Para Poder Ser Utilizada
# Como Parametro de Validação de Texto.
variacaoTexto = ctk.StringVar()

# A Função de Ajuste de Texto Recebe qualquer Caracter da Caixa de Texto Para a Execução da Função.
def ajustarTexto(*args):
    # Receve o Texto Obtido da Caixa de Texto pela Variavel variaçãoTexto.
    texto = variacaoTexto.get()
    tamanho = len(texto)

    if tamanho > 7:
        tamanhoFonte = float(50 - (tamanho + 9))
        caixaTexto.configure(font=("Segoe UI", tamanhoFonte, "bold"))
    else:
        caixaTexto.configure(font=("Segoe UI", 50, "bold"))

# Essa Função Define o Número Maximo de Caracteres Criando um Parametro Que Vai Receber
# o Número de Caracteres Atual.
def filtroCaixaTexto(textoFuturo):
    filtroCaracteres = "0123456789+-,%÷×x/"

    for char in textoFuturo:
        if char not in filtroCaracteres:
            return False # Se achar alguma letra ou caractere inválido, bloqueia!

    if len(textoFuturo) >= 18:
        return False
    elif len(textoFuturo) <= 18:
        return True

# Registra a função limitarTamanho como uma função do CTKinter, para ele identificar como uma função
# Validativa Que Pode Ser Ultilizada Pela Biblioteca.
limitarTamanho = programa.register(filtroCaixaTexto)
#endregion

#region Caixa de Texto
caixaTexto = ctk.CTkEntry(
programa,
# Recebe um Parametro de Variação de Texto
textvariable= variacaoTexto,
font=("Segoe UI", 50, "bold"),
height=80,
width=250,
# Define o Item de Validação Como o Clique do Teclado.
validate="key",
# Define o Metodo de Validação Como a função Criada Anteriormente, e Passa o Valor que o Campo terá
# Após o Clique com "%P" a Variavel de Atalho Disponivel Apenas no TKinter ou CustomTKinter.
validatecommand= (limitarTamanho, "%P"))
caixaTexto.pack(pady=15)
# O Metodo .trace_add Lê o Texto da Caixa e Aplica a Função de Acordo
variacaoTexto.trace_add("write", ajustarTexto)

# Mantem a Caixa de Texto Sempre Selecionada
programa.after(100, lambda: caixaTexto.focus_set())

#endregion Caixa de Texto

#region Função de Reconhecimento de Botão
def inserir_tecla(tecla):
    caixaTexto.insert(ctk.END, tecla)
    caixaTexto.focus_set()

def apagar():
    current_text = caixaTexto.get()
    if current_text:
        caixaTexto.delete(len(current_text) - 1, ctk.END)
    caixaTexto.focus_set()

def apagarTudo():
    current_text = caixaTexto.get()
    if current_text:
        caixaTexto.delete(0, ctk.END)
    caixaTexto.focus_set()

def enter(event=None):
    conta = caixaTexto.get()
    conta = conta.replace(",", ".")
    conta = conta.replace("÷", "/")
    conta = conta.replace("×", "*")
    conta = conta.replace("x", "*")
    conta = conta.replace("X", "*")
    if conta:
        caixaTexto.delete(0, ctk.END)
        try:
            resultado = float(sp.sympify(conta).evalf())
            resultado = round(resultado, 2)
            resultado = str(resultado)
            resultado = resultado.replace(".", ",")
            caixaTexto.insert(0, resultado)
        except:
            messagebox.showerror("Erro", "Calculo Invalido")
    caixaTexto.focus_set()
    return conta, resultado

caixaTexto.bind("<Return>", enter)
#endregion Função de Reconhecimento de Botão

#region Botões
#region Linha 3
button7 = ctk.CTkButton(linha3,
text="7", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("7"))
button7.pack(side=ctk.LEFT, padx=2)

button8 = ctk.CTkButton(linha3,
text="8", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("8"))
button8.pack(side=ctk.LEFT, padx=2)

button9 = ctk.CTkButton(linha3,
text="9", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("9"))
button9.pack(side=ctk.LEFT, padx=2)

divisao = ctk.CTkButton(linha3,
text="÷", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("÷"))
divisao.pack(side=ctk.LEFT, padx=2)
#endregion Linha 3

#region Linha 2
button4 = ctk.CTkButton(linha2,
text="4", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("4"))
button4.pack(side=ctk.LEFT, padx=2)

button5 = ctk.CTkButton(linha2,
text="5", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("5"))
button5.pack(side=ctk.LEFT, padx=2)

button6 = ctk.CTkButton(linha2,
text="6", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("6"))
button6.pack(side=ctk.LEFT, padx=2)

vezes = ctk.CTkButton(linha2,
text="×", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("×"))
vezes.pack(side=ctk.LEFT, padx=2)
#endregion Linha 2

#region Linha 1
button1 = ctk.CTkButton(linha1,
text="1", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("1"))
button1.pack(side=ctk.LEFT, padx=2)

button2 = ctk.CTkButton(linha1,
text="2", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("2"))
button2.pack(side=ctk.LEFT, padx=2)

button3 = ctk.CTkButton(linha1,
text="3", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("3"))
button3.pack(side=ctk.LEFT, padx=2)

menos = ctk.CTkButton(linha1,
text="-", 
font=("Arial", 25),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("-"))
menos.pack(side=ctk.LEFT, padx=2)
#endregion Linha 1

#region Linha 0
button0 = ctk.CTkButton(linha0,
text="0", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("0"))
button0.pack(side=ctk.LEFT, padx=2)

virgula = ctk.CTkButton(linha0,
text=",", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla(","))
virgula.pack(side=ctk.LEFT, padx=2)

porcentagem = ctk.CTkButton(linha0, 
text="%", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("%"))
porcentagem.pack(side=ctk.LEFT, padx=2)

mais = ctk.CTkButton(linha0, 
text="+", 
font=("Arial", 20),
width=60,
height=60,
fg_color="#3d3d3d",
hover_color="#383838",
command= lambda: inserir_tecla("+"))
mais.pack(side=ctk.LEFT, padx=2)
#endregion Linha 0

#region Confirmação e Delete
resultado = ctk.CTkButton(edit, 
text="=", 
font=("Arial", 25),
width=125,
height=60,
fg_color="#006EAA",
hover_color="#026397",
command= enter)
resultado.pack(side=ctk.LEFT, padx=2)

backspace = ctk.CTkButton(edit,
text="<-",
font=("Arial", 25),
width=60,
height=60,
fg_color="#BE0000",
hover_color="#A10303",
command= lambda: apagar())
backspace.pack(side=ctk.LEFT, padx=2)

limpar = ctk.CTkButton(edit,
text="C",
font=("Arial", 25),
width=60,
height=60,
fg_color="#BE0000",
hover_color="#A10303",
command= lambda: apagarTudo())
limpar.pack(side=ctk.LEFT, padx=2)
#endregion Confirmação e Delete

#region Inserção dos Botões da Tela
linha3.pack(side=ctk.TOP, pady=2)
linha2.pack(side=ctk.TOP, pady=2)
linha1.pack(side=ctk.TOP, pady=2)
linha0.pack(side=ctk.TOP, pady=2)
edit.pack(pady=2)
#endregion Inserção dos Botões da Tela
#endregion Botões

programa.bind("<Return>", lambda event: enter)

janela.mainloop()