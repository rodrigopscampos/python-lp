#Pergunte uma quantidade de itens para o usuário, 
# colete a quantidade de itens informada, 
# coloque numa lista e imprima na tela.

qtdade_itens = int(input("Quantidade de itens: "))

lista = []
i = 1
while i <= qtdade_itens:
    
    item = input("Item {}: ".format(i))
    lista.append(item)
    i = i + 1

print("Itens informados:")
for item in lista:
    print(item)


