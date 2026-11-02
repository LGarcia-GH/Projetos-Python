# Uma tupla e uma lista que o valor definido nao pode ser mudado:
# (tupla = (itens, itens2)) NOTA: normalmente tupulas usam parenteses
# ao invez de cochetes.

teste1 = (54, 73, 44)
print(teste1[0])

# NOTA: No caso de uma funcao ser utilizada e ser necessario guardar
# o valores da funcao, pode-se utilizar o unpacking da tupla que esta
# dentro da funcao:
# return valor1, valor2
# v1, v2 = nome_da_funcao

def numeros():
    numero1 = teste1[0]
    numero2 = teste1[1]
    return numero1, numero2

n1, n2 = numeros()

print(n1)
print(n2)