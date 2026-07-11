nome = input("Nome do aluno: ")

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))

frequencia = int(input("Digite a frequência (%): "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0 and frequencia >= 75:
    situacao = "Aprovado"
elif media >= 5.0 and frequencia >= 75:
    situacao = "Recuperação"
else:
    situacao = "Reprovado"

print("\n--- Resultado Final ---")
print(f"Aluno: {nome}")
print(f"Média: {media:.2f}")
print(f"Frequência: {frequencia}%")
print(f"Situação: {situacao}")