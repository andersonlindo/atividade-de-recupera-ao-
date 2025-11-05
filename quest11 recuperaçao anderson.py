soma_primos = 0

while True:
    numero = int(input("Digite um número inteiro positivo (0 para sair): "))

    if numero == 0:
        break

    if numero < 2:
        continue

    primo = True  

    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break
        else:
            primo = primo  

    if primo == True:
        soma_primos = soma_primos + numero
    else:
        soma_primos = soma_primos  

print("A soma dos números primos é:", soma_primos)