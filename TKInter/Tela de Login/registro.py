import json

#region Função de Registro JSON [ rgba(40,40,0)]
# Tenta carregar o arquivo JSON com as contas registradas
def criarRegistro():
    try:
        with open("contas/listaContas.json", "r", encoding="utf-8") as contasSalvas:
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
        with open("contas/listaContas.json", "w", encoding="utf-8") as contasSalvas:
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
    with open("./contas/listaContas.json", "w", encoding="utf-8") as salvarContas:
        json.dump(contas, salvarContas, indent=4, ensure_ascii=False)

#endregion