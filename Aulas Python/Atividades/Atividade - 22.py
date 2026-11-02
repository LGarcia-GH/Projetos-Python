num = [10, 20, 30, 40]
print(num)
print(num[2])
print(num[0:2])
print(num[1:])

num[1] = 25
print(num)

num.append(50)
print(num)

num.insert(1,15)
print(num)

num.remove(50)
print(num)

for cont in range(0,5):
    valores.append(int(input("Digite um Valor: ")))

for indice, valor in enumerate(valores):
    print(f"Na posição {indi}")