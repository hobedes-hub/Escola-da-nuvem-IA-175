"""
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:

Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""

#Definindo variáveis com os detalhes do produto
nome_produto = "cadeira_infantil"
preço_unitário = 12.40 
quantidade = 3

#Variáveis do cálculo do valor total
preço_total = preço_unitário * quantidade

print (f"produto: {nome_produto}")
print (f"preço unitário: R${preço_unitário:.2f}")
print (f"quantidade: {quantidade}")
print (f"preço unitário: R${preço_total:.2f}")

