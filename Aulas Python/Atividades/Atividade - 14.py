'contador = int(1)'

'while contador <= 10:'
'   print(contador)'
'   contador += 1'

import os

opcao = str("s")

while (opcao == "s"):
    opcao = "i"
    num1 = float(input("Digite um Número: "))
    num2 = float(input("Digite outro Número: "))
    soma = num1 + num2

    print(f"A soma de {num1:.2f} + {num2:.2f} = {soma:.2f}")

opcao = (str(input("Deseja continuar o calculo da soma de outros números?" \
"Tecle [S] para continuar ou [N] para terminar: ")))

opcao = opcao.lower

if opcao == "s":
    opcao = "s"
    os.system('cls')
else:
    os.system('exit')
