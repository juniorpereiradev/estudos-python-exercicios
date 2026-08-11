#Entrada de dados

fundo_investimento = input ("Digite o nome do fundo de investimento: ")
preco_cota = float(input("Digite o preço da cota: "))
valor_dividendo = float(input("Digite o valor do dividendo: "))
valor_investido = float(input("Digite o valor investido: "))

#Processamento de dados

numero_cotas = int(valor_investido / preco_cota)
dinheiro_gasto = numero_cotas * preco_cota
troco = valor_investido - dinheiro_gasto
rendimento_mensal = (numero_cotas * valor_dividendo)

#Saída de dados

print ("\n=== SIMULADOR DE RENDIMENTO DE INVESTIMENTO ===")
print ("="*50)
print (f"Você investiu R$ {valor_investido:.2f} no fundo {fundo_investimento}.\nO preço da cota é de R$ {preco_cota:.2f}.\nO valor do dividendo é de R$ {valor_dividendo:.2f}.\nVocê comprou {numero_cotas} cotas.\nO dinheiro gasto foi de R$ {dinheiro_gasto:.2f}.\nO troco que sobrou foi de R$ {troco:.2f}.\nO rendimento mensal do seu investimento é de R$ {rendimento_mensal:.2f}.")    
print ("="*50)

