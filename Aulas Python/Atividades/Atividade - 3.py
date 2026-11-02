import os

re = True

while re == True:
    re = False
    
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em Metros: "))

    emc = peso / (altura * altura)

    print(f"Seu EMC é de {emc}")

    print("Aperte Enter para Fechar ou R para reiniciar")
    re = input('Fechar(enter) / Reiniciar(r): ')
    if re == 'r':
        re = True
        os.system('cls')
    else:
        os.system('exit')
