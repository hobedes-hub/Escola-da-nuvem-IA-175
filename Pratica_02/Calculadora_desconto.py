"""
Desenvolva um programa que calcula o desconto em uma loja. 
Use as seguintes informações:
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

#Definindo variáveis
Nome_produto = "Camiseta"
Preço_original = 50.00
Porcentagem_desconto = 20 

#Em relação as converções
Valor_desconto = Preço_original * ( Porcentagem_desconto / 100 )
Preço_final = Preço_original - Valor_desconto

#Exibindo resultado

print(f"Produto: {Nome_produto}")
print(f"Preço original: R$ {Preço_original:.2f}")
print(f"Desconto aplicado: {Porcentagem_desconto}%")
print(f"Valor do desconto: R$ {Valor_desconto:.2f}")
print(f"Preço final com desconto: R$ {Preço_final:.2f}")