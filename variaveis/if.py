a = int( input("Primeiro número: ") )
b = int( input("Segundo número: ") )
c = int( input("Terceiro número: ") )

print("Maior: ")

r = a

if b < r:
    r = b

if c < r:
    r = c

print(r)