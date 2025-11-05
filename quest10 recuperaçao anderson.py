anterior = 1
atual = 1

for i in range(3, 38):  
    proximo = anterior + atual

    
    anterior = atual
    atual = proximo

print("O 37º termo da sequência é:", atual)