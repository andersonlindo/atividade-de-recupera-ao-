numero = int(input("Digite um número inteiro: "))
if numero < 0:
    numero = numero * -1

pares = 0
impares = 0

for i in range(10):  
    if numero == 0:
        break  

    digito = numero % 10  

    
    if digito % 2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    numero = numero // 10

print("Pares:", pares, "Ímpares:", impares)