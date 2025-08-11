from datetime import date

# 1️⃣ Função para calcular gorjeta
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    return valor_conta * (porcentagem_gorjeta / 100)


# 2️⃣ Função para verificar palíndromo
def verificar_palindromo(texto: str) -> str:
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"


# 3️⃣ Função para calcular preço final com desconto
def calcular_preco_com_desconto(preco: float, desconto: float) -> float:
    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto
    return preco_final


# 4️⃣ Função para calcular idade em dias
def calcular_idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = date.today().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365


# =====================
# Programa interativo
# =====================
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Calcular gorjeta")
        print("2 - Verificar palíndromo")
        print("3 - Calcular preço final com desconto")
        print("4 - Calcular idade em dias")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor = float(input("Digite o valor da conta: R$ "))
            porcentagem = float(input("Digite a porcentagem da gorjeta: "))
            print(f"Gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")

        elif opcao == "2":
            texto = input("Digite a palavra ou frase: ")
            print(f"É palíndromo? {verificar_palindromo(texto)}")

        elif opcao == "3":
            preco = float(input("Digite o preço do produto: R$ "))
            desconto = float(input("Digite o percentual de desconto: "))
            preco_final = calcular_preco_com_desconto(preco, desconto)
            print(f"Preço final: R$ {preco_final:.2f}")

        elif opcao == "4":
            ano_nasc = int(input("Digite o ano de nascimento: "))
            print(f"Idade em dias: {calcular_idade_em_dias(ano_nasc)} dias")

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()
