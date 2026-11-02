rodada = bool(True)
conf = str()
import os

while rodada == True:
    rodada = False
    #Variavel dos Números Coletados
    n1 = int(input("Digite o Primeiro Número: "))
    n2 = int(input("Digite o Segundo Número: "))
    cont = int(0)
    #Variavel de Diferença
    dif = n1 - n2
    #IF Para Tornar Positivo
    if n1 < n2:
        dif = (dif * -1)
    #IF para ver se um número é menor que o outro para a contagem
    if n1 < n2 or n2 < n1:
        #While para contagem dos números
        while cont <= dif:
            #Caso o Número 1 seja menor que Número 2
            if n1 <= n2:
                print(f"{n1}")
                n1 += 1
            #Caso o Número 2 seja menor que Número 1
            elif n2 <= n1:
                print(f"{n2}")
                n2 += 1
            #Andamento do Contador
            cont += 1
    #Else caso os dois números sejam iguais
    else:
        print(f"Você repetiu os dois números {n1}")

    print("Deseja fazer mais uma rodada?")
    conf = input("Sim (s) ou Não (n): ")
    conf = conf.lower()
    if conf == "s":
        os.system('cls')
        rodada = True
        conf = "i"
    else:
        os.system('exit')
