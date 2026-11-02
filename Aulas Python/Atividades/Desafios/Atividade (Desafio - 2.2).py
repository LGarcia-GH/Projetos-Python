import math

n = int(input("Digite um número: "))
r1 = int()
e = int()

for i in range(n):
    if i == 0:
        e = 2
    elif i >= 1:
        e += (1/math.factorial(i))


print(f"O Resultado é {e}")
