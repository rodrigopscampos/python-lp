#Leia um número e imprima se ele é ímpar, zero ou par

n = int(input("Informe um número: "))

if n == 0:
    print('Zero')
elif n % 2 == 0:
    print('Par')
else:
    print('Impar')