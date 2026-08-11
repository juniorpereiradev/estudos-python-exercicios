#Entrada de dados

nome_cliente = input("Digite o nome do cliente: ")
idade_cliente = int(input("Digite a idade do cliente: "))
estudante = input("O cliente é estudante? (S/N): ")
preco_ingresso = 50.00

#Processamento de dados

if idade_cliente < 18 or idade_cliente >= 60 or estudante == "S":
    resultado = preco_ingresso * 0.5
else:
    resultado = preco_ingresso

#Saída de dados

print("="*50)
print ("\n=== COMPROVANTE DE CINEMA ===".center(50))
print("="*50)
print (f"Nome do cliente: {nome_cliente}\nIdade do cliente: {idade_cliente}\nEstudante: {estudante}\nPreço do ingresso: R$ {resultado:.2f}")
print ("Você pagou meio ingresso! Aproveite o filme!")
print("="*50)




