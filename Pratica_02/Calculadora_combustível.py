"""
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. 
Use os seguintes dados:

Distância percorrida: 300 km
Combustível gasto: 25 litros 

O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,
 incluindo o resultado final arredondado para duas casas decimais.
 """

#Definindo variáveis

Distancia_percorrida = 300
Combustivel_gasto = 25

#Em relação as converções

Consumo_médio = Distancia_percorrida / Combustivel_gasto

#Exibindo resultado
print(f"Distância percorrida: {Distancia_percorrida} km")
print(f"Combustível gasto: {Combustivel_gasto} litros")
print(f"Consumo médio: {Consumo_médio} km/l")