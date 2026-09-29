#Cabeçalho do sistema

print("="*50)
print ("Sistema de cadastro".center(50))
print("="*50)

#Entrada de dados

while True:
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: R$ "))
    quantidade = int(input("Digite a quantidade do produto: "))
    descricao = input("Digite a descrição do produto: ")

    print("="*50+f"\nProduto cadastrado: {nome}\nR$ {preco:.2f}\nQuantidade: {quantidade}\nDescrição: {descricao}")
    continuar = input("Deseja cadastrar outro produto? (S/N): ")
    if continuar.lower() != "s":
        print("Cadastro de produtos encerrado.")
        break

  #Resultados

print("="*50)
print ("Resumo do cadastro".center(50))
print("="*50)
print(f"Produto: {nome}\nR$ {preco:.2f}\nQuantidade: {quantidade}\nDescrição: {descricao}")
print("="*50)





