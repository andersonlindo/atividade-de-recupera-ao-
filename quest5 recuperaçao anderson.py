num = int(input("Digite um número decimal: "))


if num == 0:
    print("0")
else:
    hexa = ""  

    
    while num > 0:
        resto = num % 16  

        
        if resto == 10:
           m         digito = 'A'
        else:
        if resto == 11:
                    digito = 'B'
         else:
         if resto == 12:
                    digito = 'C'
         else:
         if resto == 13:
                     digito = 'D'
        else:
         if resto == 14:
                     digito = 'E'
        else:
        if resto == 15:
                        
                     digito = 'F'
         else:
                     digito = str(resto)

        
        hexa = digito + hexa

        
        num = num // 16

    
    print("Hexadecimal:", hexa)