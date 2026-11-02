saAt = float(1000)
ano = int(1996)
anoAt = int(2026)
saAu = float(1.5)

dif = anoAt - ano

for i in range(dif):
    if i >= 1:
        saAu *= 2
    saAt *= saAu

print(f"O Salario final foi de R$: {saAt:.2f}")
