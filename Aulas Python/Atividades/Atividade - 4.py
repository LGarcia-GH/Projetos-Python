import os

re = True

while re == True:
    re = False
    
    distancia = float(input("Digite a distancia percorrida em Km: "))
    combustivel = float(input("Digite a quantida de combustivel em L:" ))

    media = distancia / combustivel

    print(f"O consumo médio é de {media:.2f} Km/L")

    re = print("Aperte Enter para Fechar ou R para Reiniciar")
    if re == 'r':
        r = True
        os.system('cls')
    else:
        os.system('exit')
    