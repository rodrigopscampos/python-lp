#Implemente um algoritmo que percorre uma lista de números e calcula a média

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

print("{} - Media: {}".format(lista, soma / len(lista)))