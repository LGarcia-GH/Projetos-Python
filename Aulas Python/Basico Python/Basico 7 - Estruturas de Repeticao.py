# A estrutura for, repete um codigo um numero determinado de vezes, ou
# executa conforme uma lista:
# (for i in range(numero de vezes da repeticao))
# NOTA: i e um contador de vezes que o codigo vai rodar de acordo com o
# o numero do range()

for i in range(10):
    print("funcionou")

# NOTA: outro caso mais comum e o uso do for para analisar itens em
# listas ou dicionarios para executar o codigo:

numbers = [1, 2, 3, 4, 9000, 5, 25000, 3, 2]
menor = 0
maior = 0
igual = 0
mostrar = 0

for numeros in numbers:
    if numeros > 5:
        maior += 1
    elif numeros < 5:
        menor += 1
    else:
        igual += 1

    print(f'O numero agora e: {numbers[mostrar]}')
    mostrar += 1

print(f"Numeros maior que 5: {maior}")
print(f"Numeros menor que 5: {menor}")
print(f'Numeros iguais a 5: {igual}')