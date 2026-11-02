idade = (int(input('Informe sua idade:')))

if idade >= 18:
    cnh = (str(input('Informe se você tem CNH: (s/n)')))
    if cnh == 's':
        print('Você pode dirigir')
    else:
        print('Você não pode dirigir')
else:
    print('Idade invalida')
