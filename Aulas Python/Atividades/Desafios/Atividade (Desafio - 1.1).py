#Calculadora de Equação do Segundo Grau

A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))

delta = (B**2) - (4*(A*C))

Xn = ( - B - (delta**0.5)) / (2*A)

Xp = ( - B + (delta**0.5)) / (2*A)

print(f"O resulta da equação é {Xp} e {Xn}")

input("Aperte Enter para Fechar....")







