#Entrada de dados

salario_liquido = float(input("Digite o salário líquido: "))
gasto_mensal = float(input("Digite o gasto mensal (aluguel, condominio, prestações): "))
alimentacao  = float(input("Digite o gasto mensal com alimentação: "))

#Processamento de dados

porcentagem_moradia = (gasto_mensal / salario_liquido) * 100
porcentagem_alimentacao = (alimentacao / salario_liquido) * 100
sobra = salario_liquido - gasto_mensal - alimentacao
sobra_equivale = (sobra / salario_liquido) * 100

#Saida de dados

print ("=== ANÁLISE FINANCEIRA MENSAL ===")
print (f"Voce gasta: {porcentagem_moradia:.2f}% do seu salário com moradia. \n {porcentagem_alimentacao:.2f}% do seu salário com alimentação. \n Valor restante: R$ {sobra:.2f} que equivale a {sobra_equivale:.2f}% do seu salário no final do mês.")
