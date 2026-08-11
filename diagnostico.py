#Entrada de dados

nome_paciente = input ("Digite o nome do paciente: ")
idade_paciente = int(input("Digite a idade do paciente: "))
peso_paciente = float(input("Digite o peso do paciente (em kg): "))
altura_paciente = float(input("Digite a altura do paciente (em metros): "))

#Processamento de dados

imc = peso_paciente / (altura_paciente ** 2)

#Decisões

if idade_paciente >= 60:
    pulseira = "VERMELHA"
elif imc > 30:
    pulseira = "AMARELA"
else:
    pulseira = "VERDE"


#Saída de dados

print ("="*50)
print ("TRIAGEM MÉDICA".center(50))
print ("="*50)
print (f"Nome paciente: {nome_paciente}\nIdade: {idade_paciente} anos")
print(f"IMC: {imc:.2f}")
print ("="*50)
print(f"Pulseira: {pulseira}")
print ("="*50)

       