pares = 0
impares = 0

while True:
    entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ")

    if entrada.lower() == 'fim':
        break

    try:
        numero = int(entrada)
        if numero % 2 == 0:
            print(f"{numero} é par.")
            pares += 1
        else:
            print(f"{numero} é ímpar.")
            impares += 1
    except ValueError:
        print("Erro: entrada inválida. Por favor, digite um número inteiro.")

print("\nResumo:")
print(f"Números pares inseridos: {pares}")
print(f"Números ímpares inseridos: {impares}")