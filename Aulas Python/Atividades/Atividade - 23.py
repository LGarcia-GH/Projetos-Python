import os
lista = []
parar = bool(False)
validar = bool(False)
validar2 = str()

while parar == False:
    validar = False
    numero = int(input("Digite um Número: "))
    if numero not in lista:
        lista.append(numero)
    else:
        print("Esse Número já está na lista")
    while validar == False:
        validar2 = str(input("Adicionar mais um valor (s/n)")).lower()
        if validar2 == "s" or lista == "y":
            validar = True
            validar2 == False
            parar = False
        elif validar2 == "n":
            parar == True
            validar = True
            parar = True
        else:
            print("Valor Invalido")
            validar = False

flista = sorted(lista)

print(flista)