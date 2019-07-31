# Implemente um algoritmo que percorre uma lista e encontra o maior e o menor

lista = [1, 2, 3, 4, 5, 6, -100, 100]

maior = lista[0]
menor = lista[0]

for item in lista:
    if item > maior:
        maior = item
    
    if item < menor:
        menor = item

print("Lista: " + str(lista))
print("Maior: " + str(maior))
print("Menor: " + str(menor))