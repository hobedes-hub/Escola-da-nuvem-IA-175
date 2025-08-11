import random
import string
import requests

# 1️⃣ Gerar senha aleatória
def gerar_senha():
    tamanho = int(input("Digite o tamanho da senha: "))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print(f"Senha gerada: {senha}")


# 2️⃣ Gerar perfil de usuário aleatório
def gerar_perfil_usuario():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao acessar a API Random User Generator.")


# 3️⃣ Consultar endereço pelo CEP (ViaCEP)
def consultar_endereco():
    cep = input("Digite o CEP (somente números): ")
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        if "erro" not in dados:
            print(f"Logradouro: {dados['logradouro']}")
            print(f"Bairro: {dados['bairro']}")
            print(f"Cidade: {dados['localidade']}")
            print(f"Estado: {dados['uf']}")
        else:
            print("CEP não encontrado.")
    else:
        print("Erro ao acessar a API ViaCEP.")


# 4️⃣ Consultar cotação de moeda (AwesomeAPI)
def consultar_cotacao():
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        if chave in dados:
            info = dados[chave]
            print(f"Moeda: {moeda} → Real Brasileiro (BRL)")
            print(f"Valor atual: R$ {info['bid']}")
            print(f"Valor máximo do dia: R$ {info['high']}")
            print(f"Valor mínimo do dia: R$ {info['low']}")
            print(f"Última atualização: {info['create_date']}")
        else:
            print("Moeda não encontrada.")
    else:
        print("Erro ao acessar a API AwesomeAPI.")


# =====================
# Menu interativo
# =====================
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Gerar senha aleatória")
        print("2 - Gerar perfil de usuário aleatório")
        print("3 - Consultar endereço por CEP")
        print("4 - Consultar cotação de moeda")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            gerar_senha()
        elif opcao == "2":
            gerar_perfil_usuario()
        elif opcao == "3":
            consultar_endereco()
        elif opcao == "4":
            consultar_cotacao()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu
if __name__ == "__main__":
    menu()
