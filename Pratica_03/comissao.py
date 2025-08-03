# Entrada: nome do vendedor (texto)
nome = input()

# Entrada: salário fixo (double)
salario_fixo = float(input())

# Entrada: total das vendas (double)
vendas = float(input())

# Cálculo da comissão (15% sobre vendas)
comissao = vendas * 0.15

# Cálculo do total a receber
total_receber = salario_fixo + comissao

# Saída formatada com 2 casas decimais
print(f"TOTAL = R$ {total_receber:.2f}")