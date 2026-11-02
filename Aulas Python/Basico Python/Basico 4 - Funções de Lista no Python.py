#Funcoes de lista

#Editar um item da lista:
#(lista antiga[numero do item] = valor novo)

l1 = [1, 2, "Lucas Cavalcante", 4, 5]
l1[2] = l1[2] + 10

print(l1)

print(l1[2[0:5]])


#Remover um item da lista:
#(lista.remove(texto ou numero que quer remover))

lt = ['A', 'B', 'C', 'D', 'E']
lt.remove('A')

print(lt)

#NOTA:Outro metodo:
#(lista.pop(numero da posicao da lista))

lt = ['A', 'B', 'C', 'D', 'E']
lt.pop(1)

print(lt)


#Adicionar um item a lista:
#(lista.append('nome do item))

lt.append('F')

print(lt)

#NOTA:A funcao sempre adiciona os itens no final da lista


#Adicionar itens de uma lista para outra:
#(lista.extend(nome da lista))

lt2 = ['G', 'H', 'I', "J", "K"]
lt.extend(lt2)

print(lt)

#NOTA:A funcao sempre adiciona os itens da lista no final da outra


#Inserir um item em um ponto especifico da lista:
#(lista.insert(posicao onde quer inserir, nome do item que vai inserir))

l1.insert(0, 0)

print(l1)


#Contar o numero de vezes que um item aparece na lista:
#(print(lista.count('nome do item')))

l2 = [3, 3, 3, 3]
l2.count(3)

print(l2)
print(l2.count(3))


#Ordernar uma lista em ordem:
#(lista.sort())

lt = ['F', 'A', 'a', 'G', 'd']
l1 = [7, 4, 3, 8, 1, 10]

print(lt)
print(l1)

l1.sort()
lt.sort()

print(lt)
print(l1)

#NOTA:Caso use reverse ele coloca em ordem decrescente:
#(print(lista.sort(reverse=True)))

l1.sort(reverse=True)
lt.sort(reverse=True)

print(lt)
print(l1)
