#Entrada de dados

faturamento_total = 0.0

for i in range (1, 6):
    faturamento = float(input(f"Digite o faturamento do dia: {i}: "))
    faturamento_total += faturamento
    print (f"Faturamento do dia {i}: R$ {faturamento:.2f}")

print (f"Faturamento total: R$ {faturamento_total:.2f}")
