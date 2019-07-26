#Pergunte uma quantidade de itens para o usuário,
# colete a quantidade de itens informada, coloque numa lista e imprima na tela.


#Pergunte uma quantidade de itens para o usuário,
qtd_itens = int(input("Quantidade de itens: "))
contador = 1
lista = []
#colete a quantidade de itens informada
while contador <= qtd_itens:
    #coloque numa lista
    lista.append(input("Item {} de {}: ".format(contador,qtd_itens)))
    contador = contador + 1

#imprima na tela.
print("Itens: ")
for abc in lista:
    print(abc)
