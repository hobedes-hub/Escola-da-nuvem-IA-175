while True:
    try:
        # Solicita o primeiro número
        num1 = float(input("Digite o primeiro número: "))
        
        # Solicita o segundo número
        num2 = float(input("Digite o segundo número: "))
        
        # Solicita a operação
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao not in ['+', '-', '*', '/']:
            raise ValueError("Operação inválida. Use apenas +, -, * ou /.")

        # Verifica divisão por zero
        if operacao == '/' and num2 == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")

        # Realiza a operação
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2

        print(f"Resultado: {num1} {operacao} {num2} = {resultado:.2f}")
        break  # Encerra o programa após sucesso

    except ValueError as ve:
        print(f"Erro de valor: {ve}. Tente novamente.\n")
    except ZeroDivisionError as zde:
        print(f"Erro de divisão: {zde}. Tente novamente.\n")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}. Tente novamente.\n")