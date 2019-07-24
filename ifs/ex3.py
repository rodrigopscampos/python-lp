#Leia três números e imprima o maior e o menor

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))

print('Maior:')
if a >= b and a >=c:
    print(a)
elif b >= c:
    print(b)
else:
    print(c)

print("Menor:")
if a <= b and a <=c:
    print(a)
elif b <= c:
    print(b)
else:
    print(c)