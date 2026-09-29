# Filtro de Vendas
#Cabeçalho do sistema

print("="*100)
print ("--- Sistema de filtragem de vendas ---".center (100))
print("="*100)


#Entrada de dados
total_validos = 0.0

for i in range(1, 6):
    faturamento = float(input(f"Digite o faturamento do dia {i}: "))
    if faturamento <= 0:
        print(f"Lançamento inválido/estorno detectado! ignorando valor {faturamento:.2f} do dia {i}.")
        continue      
    total_validos += faturamento

#Retorno dos resultados
print("="*100)
print(f"Faturamento semanal total: R$ {total_validos:.2f}".center(100))
print("="*100)
print("Obrigado por utilizar os nossos sistemas de filtragem de vendas!".center(100))
print("="*100)


