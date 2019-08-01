f = open('arquivo.csv', 'r')

linhas = list(f)

for linha in linhas[1:]:
    print(linha.strip())
