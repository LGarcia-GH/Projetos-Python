texto = str("Eu Adimiro o meu Brasil")
ulista = []
llista = []
for letra in texto:
    if letra.isupper():
        ulista.append(letra)
    elif letra.islower() and letra != " ":
        llista.append(letra)
print(f"Letras Maiusculas: {ulista}")
print(f"Letras Minusculas: {llista}")