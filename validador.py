# Entrada de dados
nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))
estudante = input("O cliente é estudante? (S/N): ")
preco_ingresso = 50.00

# Processamento de dados
if idade_cliente < 18 or idade_cliente >= 60 or estudante == "S" or estudante == "s":
    valor_final = preco_ingresso * 0.5
    tipo_ingresso = "MEIA-ENTRADA (50% de desconto)"
    mensagem = "Você garantiu a meia-entrada! Aproveite o filme!"
else:
    valor_final = preco_ingresso
    tipo_ingresso = "INTEIRA"
    mensagem = "Ingresso padrão emitido. Bom filme!"

# Saída de dados
print("\n" + "="*50)
print("COMPROVANTE DE CINEMA".center(50))
print("="*50)
print(f"Cliente: {nome_cliente}")
print(f"Idade: {idade_cliente} anos | Estudante: {estudante.upper()}")
print(f"Tipo de Ingresso: {tipo_ingresso}")
print(f"Valor a pagar: R$ {valor_final:.2f}")
print("-" * 50)
print(mensagem.center(50))
print("="*50)