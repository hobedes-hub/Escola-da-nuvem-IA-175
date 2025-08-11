import csv
import json
import statistics

# 1️⃣ Ler log de treinamento e calcular média e desvio padrão do tempo de execução
def analisar_log():
    arquivo = input("Digite o nome do arquivo de log (ex: log.txt): ")
    try:
        with open(arquivo, "r") as f:
            tempos = []
            for linha in f:
                linha = linha.strip()
                if linha:
                    try:
                        tempo = float(linha)  # cada linha deve ter um número (tempo)
                        tempos.append(tempo)
                    except ValueError:
                        pass  # ignora linhas não numéricas
            if tempos:
                media = statistics.mean(tempos)
                desvio = statistics.stdev(tempos) if len(tempos) > 1 else 0
                print(f"Média do tempo: {media:.2f}")
                print(f"Desvio padrão: {desvio:.2f}")
            else:
                print("Nenhum valor numérico encontrado no log.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")


# 2️⃣ Escrever dados em um arquivo CSV
def escrever_csv():
    dados = [
        ["Nome", "Idade", "Cidade"],
        ["Ana", 25, "Recife"],
        ["Bruno", 30, "São Paulo"],
        ["Carla", 28, "Rio de Janeiro"]
    ]
    with open("pessoas.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(dados)
    print("Arquivo 'pessoas.csv' criado com sucesso!")


# 3️⃣ Ler um arquivo CSV e exibir os dados
def ler_csv():
    arquivo = input("Digite o nome do arquivo CSV (ex: pessoas.csv): ")
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for linha in reader:
                print(linha)
    except FileNotFoundError:
        print("Arquivo CSV não encontrado.")


# 4️⃣ Ler e escrever dados em um arquivo JSON
def json_dados():
    pessoa = {
        "nome": "João",
        "idade": 35,
        "cidade": "Fortaleza"
    }
    # Escrever no JSON
    with open("pessoa.json", "w", encoding="utf-8") as f:
        json.dump(pessoa, f, ensure_ascii=False, indent=4)
    print("Arquivo 'pessoa.json' criado com sucesso!")

    # Ler do JSON
    with open("pessoa.json", "r", encoding="utf-8") as f:
        dados = json.load(f)
        print("Dados lidos do JSON:")
        print(dados)


# =====================
# Menu interativo
# =====================
def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Analisar log de treinamento")
        print("2 - Criar arquivo CSV com dados pessoais")
        print("3 - Ler arquivo CSV")
        print("4 - Criar e ler arquivo JSON")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            analisar_log()
        elif opcao == "2":
            escrever_csv()
        elif opcao == "3":
            ler_csv()
        elif opcao == "4":
            json_dados()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")


# Executa o menu
if __name__ == "__main__":
    menu()
