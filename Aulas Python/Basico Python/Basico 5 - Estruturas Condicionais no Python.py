#Estruturas condicionais

#if = se algo acontecer sera executado um codigo:
'if (condicao):'
'   codigo a ser executado'

n1 = int(1)
n1 += 1

if n1 == 2:
    print('funcionou')
    
    
#elif = outra condicao para executar outra possibilidade de codigo:
'if (condicao):'
'   codigo a ser executado'
'elif (condicao):'
'   codigo a ser executado'

n2 = int(2)
n2 += 1

if n2 == 4:
    print('funcionou')
elif n2 != 2:
    print('o numero nao foi o suficiente')


#else = se nao acontecer nenhuma das condicoes propostas antes:
'if (condicao):'
'   codigo a ser executado'
'elif (condicao):'
'   codigo a ser executado'
'else:'
'   codigo a ser executado'

n3 = int(2)

if n3 == 4:
    print('funcionou')
elif n3 != 2:
    print('o numero nao foi o suficiente')
else:
    print('nao funcionou')

#NOTA:Tem que ter um tab para sinalizar que esta sendo executado o codigo
#dentro do if, elif, ou else
