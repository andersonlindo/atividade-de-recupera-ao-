base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

resultado = 1

for i in range(expoente):
    if expoente == 0:
        resultado = 1
    else:
        resultado = resultado * base

print(base, "elevado a", expoente, "é:", resultado)