def celsius_to_fahrenheit(c):
    return c * 9/5 + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Entrada da temperatura
temp = float(input("Digite a temperatura: "))

# Unidade de origem
origem = input("Unidade de origem (C, F, K): ").strip().upper()

# Unidade de destino
destino = input("Unidade para converter (C, F, K): ").strip().upper()

# Verifica se as unidades são iguais
if origem == destino:
    print(f"Temperatura convertida: {temp:.2f} {destino}")
else:
    if origem == 'C':
        if destino == 'F':
            resultado = celsius_to_fahrenheit(temp)
        elif destino == 'K':
            resultado = celsius_to_kelvin(temp)
        else:
            print("Unidade destino inválida.")
            exit()
    elif origem == 'F':
        if destino == 'C':
            resultado = fahrenheit_to_celsius(temp)
        elif destino == 'K':
            resultado = fahrenheit_to_kelvin(temp)
        else:
            print("Unidade destino inválida.")
            exit()
    elif origem == 'K':
        if destino == 'C':
            resultado = kelvin_to_celsius(temp)
        elif destino == 'F':
            resultado = kelvin_to_fahrenheit(temp)
        else:
            print("Unidade destino inválida.")
            exit()
    else:
        print("Unidade origem inválida.")
        exit()

    print(f"Temperatura convertida: {resultado:.2f} {destino}")