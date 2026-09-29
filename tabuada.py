#Entrada de dados

numero = int(input("Digite um número de 1 a 10 para gerar a tabuada: "))

#Processamento de dados e cabeçalho da tabuada


while numero <1 or numero >10:
    print ("Número inválido! Digite um número entre 1 e 10.")
    numero = int(input("Digite um numero válido: "))

print ("\n" + "="*50)
print (f"Tabuada do {numero}: ".center(50))
print ("="*50)

#Resultado da tabuada
for i in range (1, 11):
    resultado = numero * i
    print (f"{numero} x {i:2d} = {resultado}".center (50))

print ("="*50)
print ("Fim da tabuada".center (50))
print ("="*50)