#O Teste
import os

#Variaveis
re = True
def verificador():
    s = True
    n = True
    pu = False
    return s, n, pu

resp = str()

#Inicio
print('''Bem vindo ao teste foda, agora você só pode digitar um sim e um não
    faça sua escolha''')
input("Digite Enter Para Continuar...")

while re == True:
    if re == True:
        verificador(re == True)
        re = False
        

#Entrada e Processamento de Dados 1       
    resp = str(input("Você é GAY?????? s/n: "))
    if (resp == "s" and s == True):
        s = False
    elif (resp == "n" and n == True):
        n = False
    elif (resp == "lucas"):
        print("VOCÊ É O MAIS HETERO POSSIVEL, FODAAA")
        pu = True
    else:
        print("resposta errada vagabundo >:(")
        pu = True
            
#Entrada e Processamento de Dados 2
    if pu == False:
        resp = str(input("Você está mentindo? s/n: "))

        if (resp == "s" and s == True or resp == "n" and n == True):
            print("( ͡° ͜ʖ ͡°)")
        elif (resp == "n" and n == False or resp == "s" and s == False):
            print("Não pode repetir a resposta Fela >:(")
        else:
            print("resposta invalida vagabundo >:(");
            
#Encerramento
    print("Digite Enter ou R para Reiniciar")
    re = input("Fechar(enter) / Reiniciar(r)")
    if re == "r":
        re = True
        s = True
        n = True
        os.system('cls')
    else:
        os.system('exit')
    
    
