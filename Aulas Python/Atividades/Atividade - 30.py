numero = [[],[],[]]
soma = int(0)
for i in range (9):
    cont = 0
    if i >= 3 and i <= 5:
        cont = 1
    if i >= 6 and i <= 8:
        cont = 2
    valor = int(input(f"Digite o {i+1}° Número: "))
    soma += valor
    numero[cont].append(valor)

for i in range (3):
    print(numero[i])

print(f"A Soma da Tabela é {soma}")