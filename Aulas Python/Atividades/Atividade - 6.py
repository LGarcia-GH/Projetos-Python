#Comparador de resultados
#Criacao de variaveis
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
comp = bool()
rei = True

#Comparacao
while rei == True:
    rei = False
    if n1 > n2 and n1 == n2:
        comp = True
    else:
        comp = False

    print(f"\nSe {n1} > {n2} e {n1} == {n2} entao o resultado e {comp}")

#Comparacao 2
    if n1 <= n2 or n1 != n2:
        comp = True
    else:
        comp = False
    
    print(f"Se {n1} <= {n2} ou {n1} != {n2} entao o resultado e {comp}")

#Comparacao 3
    if not n1 < n2:
        comp = True
    else:
        comp = False

    print(f"Se {n1} < {n2} nao for menor entao o resultado e {comp}")
    
#Encerramento do Codigo
print("\nAperte Enter para Fechar ou digite r para reiniciar: ")
confirm = str(input("Fechar(Enter) / Reiniciar(r): "))

if confirm == "r":
    rei = True
