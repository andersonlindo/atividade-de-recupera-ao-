numero = int(input("Digite um número inteiro: "))

if numero < 0:
    numero = numero * -1

maior = numero % 10

numero = numero // 10

for i in range(10):  
    if numero == 0:
        break  
    digito = numero % 10  
    if digito > maior:
        maior = digito
    else:
        maior = maior
    numero = numero // 10  

print("O dígito de maior valor é:", maior)