#Leia um número da tela e imprima todos 
#os números até zero informando se é impar ou par

n = int(input("Informe um número: "))

if n > 0:
    while n > 0:
        if n % 2 == 0:
            print(str(n) + ' = Par')
        else:
            print(str(n) + ' = Impar')
        
        n = n - 1
else:
    while n < 0:
        if n % 2 == 0:
            print(str(n) + ' = Par')
        else:
            print(str(n) + ' = Impar')
        
        n = n + 1



