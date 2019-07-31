# Implemente um algoritmo que percorre uma lista e ordene os valores

lista = [6, 5, 4, 3, 2, 1]


print("Antes: " + str(lista))


while True:
    mudou = False
    e = 0
    while e < len(lista) - 1:
        d = e + 1

        if lista[e] > lista[d]:
            aux = lista[e]
            lista[e] = lista[d]
            lista[d] = aux
            mudou = True

        e += 1

    if not mudou:
        break

print("Depois: " + str(lista))
