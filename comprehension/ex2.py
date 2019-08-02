#Crie uma lista de números com valores repetidos e remova-os utilizando um set

entrada = list(range(0,10)) * 3
saida = list(set(entrada))

print("Entrada: " + str(entrada))
print("Saída: " + str(saida))