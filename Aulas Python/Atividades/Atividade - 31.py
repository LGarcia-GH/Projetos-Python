import os
matriz1 = [[],[]]
matriz2 = [[],[]]
matrizS = [[],[]]

for i in range(4):
    cont = 0
    if i >= 2 and i <= 3:
        cont = 1

    valor = int(input(f"Digite o {i+1}° Número da Matriz 1: "))
    matriz1[cont].append(valor)

for i in range(4):
    cont = 0
    if i >= 2 and i <= 3:
        cont = 1

    valor = int(input(f"Digite o {i+1}° Número da Matriz 2: "))
    matriz2[cont].append(valor)

for i in range(4):
    if i < 2:
        soma = matriz1[0][i]
        soma2 = matriz2[0][i]
        soma += soma2
        matrizS[0].append(soma)
    elif i >=2:
        soma = matriz1[1][i-2]
        soma2 = matriz2[1][i-2]
        soma += soma2
        matrizS[1].append(soma)

os.system('cls')

print("-------Matriz-1-------")

for i in range (2):
    print(f"        {matriz1[i]}        ")

print(" ")
print("-------Matriz-2-------")

for i in range (2):
    print(f"        {matriz2[i]}        ")

print(" ")
print("----Soma-da-Matriz----")

for i in range(2):
    if i == 0:
        print(f"        {matrizS[i]}        ")
    else:
        print(f"        {matrizS[i]}        ")