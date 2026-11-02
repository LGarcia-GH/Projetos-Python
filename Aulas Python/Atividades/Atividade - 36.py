lista = []
pessoa = {}
soma = 0
media = 0

while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: '))
    pessoa['Sexo'] = str(input('Sexo [M/F]: ').upper())
    pessoa['Idade'] = int(input('Idade: '))
    soma += pessoa['Idade']
    lista.append(pessoa.copy)
    resp = str(input('Quer Continuar? [S/N] ')).upper()
    if resp == 'N':
        break
print(lista)
print(f'Ao todo temos {len(lista)} Pessoas Cadastradas.')
media = soma / len(lista)
print(f'A Media de Idade é de {media:.2f} Anos')
print(f'As Mulheres Cadastradas Foram: ')
for p in lista:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ')