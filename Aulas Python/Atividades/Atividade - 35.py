jogador = {}
partidas = []

jogador['Nome'] = str(input('Nome do Jogador: '))
total = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {c}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print(jogador)