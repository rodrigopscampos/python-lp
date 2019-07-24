#Leia um número da tela e imprima a tabuada de 0 a 10

n = int(input('Digite um número: '))

x = 0

while x <= 10:
    print(str(n) + " X " + str(x) + " = " + str(n * x))
    x = x + 1