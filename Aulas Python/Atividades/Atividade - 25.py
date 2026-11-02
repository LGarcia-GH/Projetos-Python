lista = [-1, 6, -9, -8, 4, 0, -3, 2, 7, 1, 8, -2]
olista = []
plista = []
nlista = []

for num in lista:
    if num >= 0:
        plista.append(num)
    elif num < 0:
        nlista.append(num)

olista = sorted(lista)


print(f"Lista Original: {lista}")
print(f"Lista Ordenada: {olista}")
print(f"Lista Positivo: {plista}")
print(f"Lista Negativo: {nlista}")