nome_vendedor = str(input("Digite o nome do vendedor: "))

salario_fixo = float(input("Digite o salário do vendedor: "))
vendas = float(input("Digite o valor total das Vendas: "))

total = salario_fixo + (vendas * 0.15)
print(f"O valor s receber do colaborador {nome_vendedor} é fr R$ {total:.2f}")