n = int(input("Digite um número inteiro positivo: "))

soma_fatoriais = 0

for i in range(1, n + 1):

    fatorial = 1
    for j in range(1, i + 1):
        fatorial = fatorial * j

    soma_fatoriais = soma_fatoriais + fatorial

print("A soma dos fatoriais de 1 até", n, "é:", soma_fatoriais)