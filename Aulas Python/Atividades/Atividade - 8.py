nc = int(input('Digite a quantidade de cadeiras que vai comprar: '))
preco = float()
precoF = float()

if nc > 50:
    preco = 40
    precoF = preco * nc
    print(f'O custo será de R$:{precoF} sendo R$:{preco} o valor unitario')
elif nc <= 50 and nc > 0:
    preco = 45
    precoF = preco * nc
    print(f'O custo será de R$:{precoF} sendo R$:{preco} o valor unitario')
else:
    print('Número invalido')
    