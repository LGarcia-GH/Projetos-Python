#Estrutura de dicionario

#Dicionario e uma lista com valor associado:
#(dicionario = {'item1':1, 'item2':2, 'item3':3})

d = {'laranja':6, 'uva':5, 'manga':8}

print(d)
print(d['uva'])


#Editar o valor de um item do dicionario:
#(dicionario['item'] = novo valor)

d['laranja'] = 15

print(d)


#Remover um item do dicionario:
#(dicionario.pop('nome do item'))

d.pop('manga')

print(d)


#Verificar um item do dicionario:
#(print('item' in dicionario))

print('uva' in d)

#NOTA:Outro metodo:
#(print('item' in dicionario.keys( )))

print('laranja' in d.keys())

#NOTA:Voce pode usar o valor do item na verificacao:
#(print(valor do item.values( )))

print(5 in d.values())


#Transformar um dicionario em uma lista:
#(lista = list(nome do dicionario))
#NOTA:Voce pode imprimir apenas o valor como lista ou as chave

l = list(d)
l2 = list(d.keys())
n = list(d.values())

print(l)
print(l2)
print(n)
