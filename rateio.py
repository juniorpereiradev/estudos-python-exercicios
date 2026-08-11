#Entrada de dados

valor_total = float(input("Digite o valor total do rateio: "))
horas_fullstack = float(input("Digite o número de horas do fullstack: "))
horas_designer = float(input("Digite o número de horas do designer: "))
horas_gestor = float(input("Digite o número de horas do gestor: "))

#Processamento de dados

pontos_totais = (horas_fullstack * 3) + (horas_designer * 2) + (horas_gestor * 1)
valor_ponto = valor_total / pontos_totais
pagamento = (horas_fullstack * 3 * valor_ponto, horas_designer * 2 * valor_ponto, horas_gestor * 1 * valor_ponto)

#Saída de dados

print ("\n=== FOLHA PAGAMENTO ===")
print ("="*30)
print (f"Valor total do rateio: R$ {valor_total:.2f}")
print ("-"*30)
print (f"Horas do fullstack: {horas_fullstack}")
print ("-"*30)
print (f"Horas do designer: {horas_designer}")
print ("-"*30)
print (f"Horas do gestor: {horas_gestor}")
print ("-"*30)
print (f"Pontos totais: {pontos_totais}")
print ("-"*30)
print (f"Valor por ponto: R$ {valor_ponto:.2f}")
print ("-"*30)
print (f"Pagamento - Fullstack: R$ {pagamento[0]:.2f}")
print ("-"*30)
print (f"Pagamento - Designer: R$ {pagamento[1]:.2f}")
print ("-"*30)
print (f"Pagamento - Gestor: R$ {pagamento[2]:.2f}")
print ("="*30)

