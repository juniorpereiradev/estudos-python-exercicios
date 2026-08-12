#Entrada de dados

nome_cliente = input ("Digite o nome do cliente: ")
salario_bruto_mensal = float(input("Digite o salário bruto mensal: "))
valor_total_imovel = float(input("Digite o valor total do imóvel: "))
quantidade_anos = int(input("Digite a quantidade de anos para o financiamento: "))


#Processamento de dados

quantidade_meses = quantidade_anos * 12
valor_parcela_mensal = valor_total_imovel / quantidade_meses
limite_comprometimento = salario_bruto_mensal * 0.3

#Decisões

if valor_parcela_mensal <= limite_comprometimento:
    resultado = "Aprovado"
else:
    resultado = "Reprovado"


    #Saída de dados

print ("\n=== SIMULADOR DE FINANCIAMENTO IMOBILIÁRIO ===")
print ("="*50)
print (f"Nome do cliente: {nome_cliente}\nSalário bruto mensal: R$ {salario_bruto_mensal:.2f}\nValor total do imóvel: R$ {valor_total_imovel:.2f}\nQuantidade de anos para o financiamento: {quantidade_anos}\nQuantidade de meses para o financiamento: {quantidade_meses}\nValor da parcela mensal: R$ {valor_parcela_mensal:.2f}\nLimite de comprometimento (30% do salário): R$ {limite_comprometimento:.2f}\nResultado da análise: {resultado}")
print ("="*50)      
