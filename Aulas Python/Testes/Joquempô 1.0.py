#Joquempô
'Import da função de número aleatorios'
import random
'import da função de comandos'
import os

#Variaveis

confirm = str()
restart = 1
re = ["Pedra", "Papel", "Tesoura"]

#Entrada de Dados

print("Bem vindo ao Joquempô 1.0\n")

while restart == 1:
    restart = restart - 1

    esc1 = int(input("Escolha: 0(Pedra) - 1(Papel) - 2(Tesoura)"))
    esc2 = random.randint(0, 2)

    #Processamento de Dados
        
    if esc2 == 0 and esc1 == 1 or esc2 == 1 and esc1 == 2 or esc2 == 2 and esc1 == 0:
        print(f"Você usou: {re[esc1]}")
        print(f"E ganhou de: {re[esc2]}: ")
    elif esc2 == esc1:
        print(f"Você usou: {re[esc1]}")
        print(f"E empatou com: {re[esc2]}")
    else:
       print(f"Você usou: {re[esc1]}")
       print(f"E perdeu para: {re[esc2]}")

    #Final
    
    print("Aperte Enter para Fechar ou digite r para reiniciar: ")
    confirm = str(input("Fechar(Enter) / Reiniciar(r): "))

    if confirm == "r":
        restart += 1
        os.system('cls')
    else:
        os.system('exit')



    
    




    

    


