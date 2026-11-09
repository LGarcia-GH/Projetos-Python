import json
from pathlib import Path

# Pega o diretório onde o arquivo atual (registro.py) está salvo
base_dir = Path(__file__).resolve().parent


# Define o caminho completo usando a barra '/' para juntar as pastas
caminho_arquivo = base_dir / "contas" / "listaContas.json"
contasP = base_dir / "contas"

# Garante que a pasta 'contas' exista (equivalente ao os.makedirs)
caminho_arquivo.parent.mkdir(parents=True, exist_ok=True)

#region Função de Registro JSON [ rgba(40,40,0)]
# Tenta carregar o arquivo JSON com as contas registradas
def criarRegistro():
    contasP.mkdir(parents=True, exist_ok=True)

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as contasSalvas:
            contas = json.load(contasSalvas)
            print("Arquivo Carregado!")
    # Caso ele não consiga carregar o arquivo ele ira gerar um novo dicionario e ao final do codigo criar um no arquivo JSON
    except FileNotFoundError:
        contas = {
            "emailUsuario": {"adm@gmail.com":"adm"},
            "senha": ["Admininastror"],
            "idade": [22],
            "superUsuario": [1]
        }
        #Salva o novo arquivo JSON com o novo dicionario 
        with open(caminho_arquivo, "w", encoding="utf-8") as contasSalvas:
            json.dump(contas, contasSalvas, indent=4, ensure_ascii=False)
        print("Arquivo Inexistente!")

        print("Um Novo Dicionario Foi Criado")
    #Caso o arquivo JSON já exista e não possua nenhum dado, o programa informa que o arquivo está vazio porem vai executar da mesma forma
    except json.JSONDecodeError:
        print("O Arquivo Existe Porem Não Há Dados!")
        contas = {
            "emailUsuario": {},
            "senha": [],
            "idade": []
        }
    return contas
#endregion

#region Salvar Registro
def salvarRegistro(contas):
    with open(caminho_arquivo, "w", encoding="utf-8") as salvarContas:
        json.dump(contas, salvarContas, indent=4, ensure_ascii=False)
#endregion