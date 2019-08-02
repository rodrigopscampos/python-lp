# Transforme uma lista de números em um dicionário de chave
# número e valor quantidade de números na lista

entrada = [
    1, 
    2, 2, 
    3, 3, 3, 
    4, 4, 4, 4
]

#forma menos difícil
def contar(lista, n):
    return len([i for i in lista if i == n])

saida = {i: contar(entrada, i) for i in entrada}

#forma difícil
#saida = {i: len([a for a in entrada if a == i]) for i in entrada}

print(saida)
