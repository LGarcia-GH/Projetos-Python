idade = int(input('Digite a idade do funcionario: '))

if idade > 30:
    Aempresa = int(input('Digite o tempo em anos de serviços prestados a empresa: '))
    if Aempresa > 3:
        salario = (float(input('Digite o salario do funcionario: ')))
        if salario <= 4000:
            print(f'O funcionario tem {idade} anos, {Aempresa} anos de serviço prestados e um salario de R$:{salario:.2f}')
            print('O reajuste está disponivel para o funcionario')
        else:
            print('Salario muito elevado para um reajuste')
    else:
        print('Tempo de serviços prestados insuficiente para um reajuste')
else:
    print('Idade insuficiente para um reajuste')
