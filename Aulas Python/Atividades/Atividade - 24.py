import os
lista = []
plista = []
ilista = []
parar = bool(False)
validar = bool(False)
validar2 = str()

while parar == False:
    validar = False
    numero = int(input("Digite um Número: "))
    if numero not in lista:
        lista.append(numero)
        if numero % 2 == 0:
            plista.append(numero)
        elif numero  % 2 != 0:
            ilista.append(numero)
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
    os.system('cls')

flista = sorted(lista)
plista = sorted(plista)
ilista = sorted(ilista)

print(f"Lista de Números Completa: {flista}")
print(f"Lista de Números Pares: {plista}")
print(f"Lista de Números Impares: {ilista}")