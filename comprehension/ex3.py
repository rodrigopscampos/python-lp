# Transforme uma lista de números em uma lista de tuplas com o número, o anterior e o próximo

entrada = list(range(0, 11))
saida = [(i-1, i, i+1) for i in entrada]

print("Entrada: " + str(entrada))
print("Saída: " + str(saida))
