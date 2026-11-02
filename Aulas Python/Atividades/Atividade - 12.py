Ecivil = {'s':'Solteiro', 'c':'Casado', 'd':'Divorsiado', 'v':'Viuvo'}

print('Digite seu estado Civil:')
print('Solteiro   (s)')
print('Casado     (c)')
print('Divorsiado (d)')
print('Viuvo      (v)')

res = str(input().lower())

if res in Ecivil:
    print(Ecivil[res])
else:
    print('Valor invalido')
