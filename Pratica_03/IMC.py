# Solicita peso em kg
peso = float(input("Digite o peso em kg: "))

# Solicita altura em metros
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Classificação do IMC
if imc < 18.5:
    classificacao = "Abaixo do peso"
elif imc < 25:
    classificacao = "Peso normal"
elif imc < 30:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obeso"

# Exibe o resultado com 2 casas decimais no IMC
print(f"IMC: {imc:.2f}")
print(f"Classificação: {classificacao}")