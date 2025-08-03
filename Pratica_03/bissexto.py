# Solicita o ano
ano = int(input("Digite o ano: "))

# Verifica se é bissexto
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    print(f"{ano} é bissexto.")
else:
    print(f"{ano} não é bissexto.")