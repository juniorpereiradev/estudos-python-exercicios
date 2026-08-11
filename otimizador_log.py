#Entrada de dados

nome_produto = input("Digite o nome do produto: ")
peso_produto = float(input("Digite o peso do produto (em kg): "))
preco_total = float(input("Digite o preço total do lote: "))

#Procesamento de dados

taxa_marketplace = preco_total * 0.065
custo_combustivel_kg = 3.20
seguro_carga = 0.008
lucro_liqudo = (preco_total - taxa_marketplace - (custo_combustivel_kg * peso_produto) - (seguro_carga * preco_total))
margem_lucro = (lucro_liqudo / preco_total) * 100


#Saída de dados

print ("\n=== ANÁLISE DE LUCRO DO PRODUTO ===")
print ("="*40)
print (f"O custo do peso do produto é de R$ {custo_combustivel_kg * peso_produto:.2f}.\nO custo do seguro da carga é de R$ {seguro_carga * preco_total:.2f}.\nO lucro líquido do produto é de R$ {lucro_liqudo:.2f}.\nA margem de lucro é de {margem_lucro:.2f}%.")
print ("="*40)
print ("\nObrigado por utilizar o Otimizador de Lucro do Produto!")
