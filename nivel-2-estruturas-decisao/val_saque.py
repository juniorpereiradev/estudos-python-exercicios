#Entrada de dados

nome_cliente = input("Digite o nome do cliente: ")
senha = int(input("Digite a senha do cliente: "))
senha_cadastrada = 1234
saldo_cliente = 5000.00

#Processamento

if senha == (senha_cadastrada):
    print("Acesso permitido.\n")
    valor_saque = float(input("Digite o valor do saque: "))
    if valor_saque <= saldo_cliente:
        saldo_atual = saldo_cliente - valor_saque
        print("Saque realizado com sucesso.\n")

        #Saida de dados de senha correta
        print("\n" + "=" * 50)
        print("EXTRATO BANCÁRIO".center(50))
        print("=" * 50)
        print(f"Cliente: {nome_cliente}")
        print(f"Saldo anterior: R$ {saldo_cliente:.2f}")
        print(f"Valor do saque: R$ {valor_saque:.2f}")
        print("-" * 50)
        print(f"Saldo atual: R$ {saldo_atual:.2f}")
        print("=" * 50)
        
    else:
        print("Saldo insuficiente para realizar o saque.")
        saldo_atual = saldo_cliente
else:
    print("Senha incorreta. Acesso negado.\n")

    #Saida de dados de senha incorreta
    print("\n" + "=" * 50)
    print("ERRO DE AUTENTICAÇÃO".center(50))
    print("=" * 50)
    print("Senha Incorreta! Operação Cancelada.")
    print("=" * 50)
