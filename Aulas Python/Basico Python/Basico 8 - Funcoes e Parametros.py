# def e o comando usado para definir uma funcao
# NOTA: Funcao e um conteainer de codigos predefinidos pelo programador,
# que pode ser usado depois apenas digitando a o nome da funcao.
# (def "nome da funcao"(parametro[opcional]):)

def calculo():
    n1 = float(input('Digite o primeiro numero: '))
    n2 = float(input('Digite o segundo numero: '))
    soma = float(n1 + n2)
    return print(soma)

# NOTA: para executar a funcao digite o nome dela e parenteses para
# chama-la.

calculo()