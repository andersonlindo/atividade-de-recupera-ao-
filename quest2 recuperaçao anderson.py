num=int(input("digite um numero decimal: "))
binario=0
base=1

for i in range(32):
    if num == 0: 
        break
    resto=num % 2
    binario += resto * base 
    base *= 10
    num //=2

print("numero em binario:", binario)