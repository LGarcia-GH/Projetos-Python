numero = [[],
          [],
          [],
          [],
          []]
soma = int(0)

for i in range (10):
    cont = 0
    if i >= 2 and i <= 3:
        cont = 1
    if i >= 4 and i <= 5:
        cont = 2
    if i >= 6 and i <= 7:
        cont = 3
    if i >= 8:
        cont = 4

    valor = int(input(f"Digite o {i+1}° Número: "))
    soma += valor
    numero[cont].append(valor)


for i in range (5):
    print(numero[i])

print(f"A Soma da Tabela é {soma}")