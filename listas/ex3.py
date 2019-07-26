#Implemente um algoritmo que percorre uma lista, some os valores e imprima

lista = []
while True:
    texto = input("Digite um número ou pressione Enter para continuar: ")

    if texto == "":
        break
    else:
        lista.append(texto)


soma = 0
for item in lista:
    soma += int(item)

print("{} - Soma: {}".format(lista, soma))



