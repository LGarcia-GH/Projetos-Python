idade = int(input('Digite sua idade: '))

if idade < 18 and idade > 0:
    print(f'Você é menor de idade com: {idade} anos')
elif idade >= 18:
    print(f'Você é maior de idade com: {idade} anos')
else:
    print('Idade invalida')
