valorP = float(input('Digite o valor do produto: '))
desconto = float()

if valorP > 0:  
    tipoP = int(input('Metodo de Pagamento: à vista(1) / à prazo(2)'))
    
    if tipoP == 1:
        desconto = valorP * 0.10
        valorP -= desconto
        print(f'O Preço é de R$:{valorP}, sendo R$:{desconto} o valor do desconto')
        print('Metodo de pagamento: À Vista')
    elif tipoP == 2:
        print(f'O Preço é de R$:{valorP}, sem desconto')
        print('Metodo de pagamento: À Prazo')
    else:
        print('Metodo de pagamento invalido')
else:
    print('Valor invalido')
