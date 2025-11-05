maior_peso_m = 0
nome_mais_pesado_m = ""

maior_altura_f = 0
nome_mais_alta_f = ""

soma_idades = 0
total_atletas = 0

for i in range(1000):  
    nome = input("Digite o nome do atleta (ou '@' para sair): ")

    if nome == "@":
        break

    sexo = input("Digite o sexo (M/F): ")
    idade = int(input("Digite a idade: "))
    peso = float(input("Digite o peso (kg): "))
    altura = float(input("Digite a altura (m): "))

    soma_idades = soma_idades + idade
    total_atletas = total_atletas + 1

    if sexo == "M" or sexo == "m":
        if peso > maior_peso_m:
            maior_peso_m = peso
            nome_mais_pesado_m = nome
        else:
            maior_peso_m = maior_peso_m

    else:
        if altura > maior_altura_f:
            maior_altura_f = altura
            nome_mais_alta_f = nome
        else:
            maior_altura_f = maior_altura_f

if total_atletas > 0:
    media_idades = soma_idades / total_atletas
else:
    media_idades = 0

print("Atleta masculino com maior peso:", nome_mais_pesado_m)
print("Atleta feminina com maior altura:", nome_mais_alta_f)
print("Média de idade dos atletas:", media_idades)