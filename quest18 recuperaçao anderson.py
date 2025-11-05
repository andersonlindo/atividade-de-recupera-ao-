n = int(input("Digite a quantidade de números: "))

soma = 0.0
menor = 0.0
maior = 0.0

for i in range(n):
    num = float(input("Digite um número real: "))

    if i == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        else:
            menor = menor

        if num > maior:
            maior = num
        else:
            maior = maior

    soma = soma + num

media = soma / n

print("Menor número:", menor)
print("Maior número:", maior)
print("Média aritmética:", media)