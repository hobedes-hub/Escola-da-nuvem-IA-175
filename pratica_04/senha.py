def senha_forte(senha):
    if len(senha) < 8:
        print("A senha deve ter pelo menos 8 caracteres.")
        return False
    if not any(char.isdigit() for char in senha):
        print("A senha deve conter pelo menos um número.")
        return False
    return True

while True:
    senha = input("Digite uma senha (ou 'sair' para encerrar): ")

    if senha.lower() == 'sair':
        print("Encerrando o programa.")
        break

    if senha_forte(senha):
        print("Senha forte cadastrada com sucesso!")
        break