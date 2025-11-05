numero = int(input("Digite um número inteiro: "))

if numero < 0:
    numero = -numero

soma = 0

while numero > 0:
    digito = numero % 10       
    soma = soma + digito       
    numero = numero // 10      

print("A soma dos dígitos é:", soma)