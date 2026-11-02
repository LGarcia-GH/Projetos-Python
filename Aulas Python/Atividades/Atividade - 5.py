vendedor = str(input("Digite o nome do vendedor: "))

salarioM = float(input("Digite o salario minimo: "))

numeroV = int(input("Digite o número de vendas: "))

salarioF = salarioM + (numeroV * 0.15)

print(f"O salario final do vendedor {vendedor} é de R$:{salarioF:.2f}")

input("Aperte Enter para Fechar....")
