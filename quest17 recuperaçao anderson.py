inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

if inicio > fim:
    print("Intervalo inválido. O início deve ser menor que o fim.")
else:
    contador_primos = 0

    for numero in range(inicio, fim + 1):
        if numero > 1:
            eh_primo = True

            for i in range(2, numero):
                if numero % i == 0:
                    eh_primo = False
                    break
                else:
                    eh_primo = eh_primo

            if eh_primo == True:
                contador_primos = contador_primos + 1
            else:
                contador_primos = contador_primos
        else:
            contador_primos = contador_primos

    print("Quantidade de números primos no intervalo:", contador_primos)