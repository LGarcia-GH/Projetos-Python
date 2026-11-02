#--Funções de Formatação do Python--#

#Formatar Casas Decimais Após a Virgula:
#(round("número de casas decimais"))
#Ou (print(f'{variavel:.2f}'))

n1 = float(5.085)
print(round(n1, 2))
print(f'{n1:.2f}')

#Formatar todo o texto em Maiusculo:
#(variavel.upper( ))

le = 'teste'
le = le.upper()
print(le)

#Formatar todo o texto em Minusculo:
#(variavel.lower( ))

le = le.lower()
print(le)

#Encontra a Posição de um Caracter a sua escolha no texto:
#(variavel.find("carater"))

le = le.find('s')
print(le)
#NOTA: O resultado será -1 quando não for encontrado o caracter

#Encontra o Número de Caracteres do texto:
#(print(len(variavel_qualquer)))

le = 'teste'
print(len(le))

#Pegar um Caracter Expecifico de um texto:
#(print(variavel_qualquer[numero/variavel]))

print(le[3])
#NOTA: A função dara erro se o número do caracter não for encontrado
#NOTA: Caso queira pegar uma parte do texto use:
#([posicao do primeiro caractere : posicao ate ultimo caracter])

print(le[0:3])

#Substituir uma parte do texto:
#(variavel_nova = variavel_antiga.replace('parte do texto', 'novo texto'))

leN = le.replace('ste', 'xto')
print(leN)
#NOTA: A função vai lhe dar o resultado  sem substituição

#Deixar a Primeira Letra do texto Maiuscula:
#(print(variavel.capitalize( ))) - Deixa apenas a Primeira Letra Maiuscula
#(print(variavel.title( ))) - Deixa Toda Primeira Letra de Cada Palavra Maiuscula

nome = 'lucas cavalcante'
print(nome.capitalize())
print(nome.title())

#Formatar em porcentagem:
#(print(f'{variavel:.(numero de casas apos a virgula)%)}')

print(f'{n1:.2%}')
