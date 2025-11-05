numero = int(input("Digite um número inteiro positivo: "))

soma_divisores = 0

for i in range(1, numero):

    if numero % i == 0:
        soma_divisores = soma_divisores + i
    else:
        soma_divisores = soma_divisores

if soma_divisores == numero:
    print(numero, "é um número perfeito.")
else:
    print(numero, "não é um número perfeito.")