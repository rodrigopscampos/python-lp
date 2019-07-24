#Leia um número e imprima se ele é positivo, negativo ou zero

n = int(input("Informe um número: "))

if n == 0:
    print('Zero')
elif n > 0:
    print('Positivo')
else:
    print('Negativo')