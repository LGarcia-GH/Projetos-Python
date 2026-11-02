palavra = str("TESTE")
erro = int()
forca = "-" * len(palavra)
numP = int(len(palavra))

while erro < numP - 1 or letra.find(letra) != -1:
	print(forca)
	letra = input(str(("Digite uma Letra...."))).upper()

	posiP = palavra.find(letra)

	for i in range (len(palavra)):
		if palavra[letra] == letra:
			forca = forca[:posiP] + letra + forca[posiP + 1:]
	else:
		erro += 1
	
	print(forca)