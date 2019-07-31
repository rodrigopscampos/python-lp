# Encontrei o segundo menor e segundo maior

lista = [10, 10, 11, 12]

lista.sort()
lista = list(set(lista))

maior = lista[1] # 12
menor = lista[-2] # 10

for item in lista:
    if item > maior:
        maior = item
    
    if item < menor:
        menor = item

segundo_maior = menor # 10
segundo_menor = maior # 10
for item in lista:
    if item != menor and item < segundo_menor:
        segundo_menor = item
    
    if item != maior and item > segundo_maior:
        segundo_maior = item
        
print("Menor: " + str(menor))
print("Maior: " + str(maior))
print("Segundo Menor: " + str(segundo_menor))
print("Segundo Maior: " + str(segundo_maior))
