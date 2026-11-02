import os

print('Bem vindo ao separador de Menor e Maior Número')
input('Aperte Enter pra Continuar...')

def menor_maior():
    repetir = bool(True)
    re = str()
    maior = float()
    menor = float()
    i = int(1)
    while repetir == True:
        if i == - 1:
            i = 1
        repetir = False
        n = float(input(f'Digite o {i}° Número: '))
        if n > maior and n > 0:
            maior = n
        if n < maior and n > 0:
            menor = n

        if n <= 0:
            print('O Número Digitado não Pode ser Igual ou Menor que 0')
            repetir = True
        else:
            print('Digite Enter para Continuar ou R para Adicionar mais um Número')
            re = input('Continuar(enter) Adicionar(a)')
            re = re.lower()
            if re == "a":
                repetir = True
                i += 1
            else:
                re == "i"
                repetir = False
                print(f'O menor número é o {menor}, e o maior é o {maior}')
                print('Digite R para reiniciar ou Enter para Continuar: ')
                re = str(input('Reiniciar(r): Fechar(enter): '))
                re = re.lower()
                if re == "r":
                    repetir = True
                    i = -1
                    os.system('cls')
                else:
                    os.system('exit')

menor_maior()
