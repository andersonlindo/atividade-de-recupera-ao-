num = int(input("digite um numero: "))
produto=1
tempo= num 
cont=0
n= tempo
while n>0:
    cont +=1
    n //=10
for i in range(cont):
    digitos=num %10
    produto *= digitos
    num //=10

print("produto dos digitos:", produto)

