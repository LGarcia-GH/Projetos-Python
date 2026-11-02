import os

re = True


while re == True:
    re = False
    aluno = str(input("Digite o nome do aluno: "))
    n1 = float(input("Digite a primeira nota: "))
    n2 = float(input("Digite a segunda nota: "))
    n3 = float(input("Digite a terceira nota: "))
    n4 = float(input("Digite a quarta nota: "))

    media = (n1 + n2 + n3 + n4) / 4

    print(f"A média de {aluno} é de: {round(media, 2)}")
    
    print("Aperte Enter para Fechar ou R para reiniciar")
    re = input('Fechar(enter) / Reiniciar(r)')
    if re == 'r':
        re = True
        os.system('cls')
    else:
        os.system('exit')
