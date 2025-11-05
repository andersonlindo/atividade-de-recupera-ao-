numero = int(input("Digite um número inteiro: "))


if numero < 0:
    numero = numero * -1

original = numero


invertido = 0

for i in range(10):  
    if numero == 0:
        break
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

if original == invertido:
    print("O número é palíndromo.")
else:
    print("O número não é palíndromo.")