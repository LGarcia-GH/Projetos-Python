import os
nomesL = []
idadesL = []

n = int(input("Digite Quantas Pessoas quer Registrar: "))
os.system('cls')

for i in range(n):
    nome = str(input(f"Digite o {i+1} Nome: "))
    nomesL.append(nome)
    idade = int(input(f"Digite a {i+1} Idade: "))
    idadesL.append(idade)
    os.system('cls')

for i in range(n):
    print(f"{nomesL[i]} tem {idadesL[i]} anos")
    if idadesL[i] >=18:
        print(f"{nomesL[i]} é maior de idade")
    else:
        print(f"{nomesL[i]} é menor de idade")
    print("-----------------------------------")
    