#Print de Tuplas
num = (10, 20, 30, 40)
print(num)
print(num[2])
print(num[0:2])
print(num[1:])

#Estrutura de Repetição
for contador in num:
	print(contador)

print("\n")

for contador in range (0, len(num)):
	print(num[contador])

print(" ")

#Mostrando a posição do valor
for contadorPos, contadorValor in enumerate(num):
	print(f"Posição {contadorPos} Tem o valor {contadorValor}")

print("\n")

for contador in range (0, len(num)):
	print(f"Posição {contador} tem o valor {num[contador]}")

#Alteração de Tuplas (não se altera)
num = (10, 20, 30, 40)
num[2] = 55
print(num[2])
