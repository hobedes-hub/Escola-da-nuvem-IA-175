"""
Crie um programa que converte um valor em reais para dólares e euros.
O programa deve calcular e exibir os valores convertidos, 
arredondando para duas casas decimais. 
"""

#Definido as variáveis

valor_reais = 100.00
taxa_dólar = 5.60
taxa_euro = 6.60 

# Realizando as conversões
valor_dolar = valor_reais / taxa_dólar
valor_euro = valor_reais / taxa_euro

# Exibindo os resultados com duas casas decimais
print(f"Valor em reais: R$ {valor_reais:.2f}")
print(f"Convertido para dólares: US$ {valor_dolar:.2f}")
print(f"Convertido para euros: € {valor_euro:.2f}")