aluno = {}
aluno['nome'] = str(input("Nome de aluno: "))
aluno['media'] = float(input("Média do aluno: "))

print(aluno)

print(f"Nome = {aluno['nome']}")
print(f"Média = {aluno['media']}")

if aluno['media'] >= 6:
    aluno['situacao'] = "Aprovado"
else:
    aluno['situacao'] = "Reprovado"
    print(f"Situação = {aluno['situacao']}")