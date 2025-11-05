num= int(input("digite um numero: "))
contador=0
tempo=num 

for i in range(num):
    if tempo ==0:
        break
    tempo //=10
    contador +=1

print("quantidade de digitos:",contador)