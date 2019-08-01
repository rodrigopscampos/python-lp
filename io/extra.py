# A ultima coluna do arquivo.csv (Selecione Tipo de CE Simp 4)
# possui dois números separados por vírgula
# O desafio é fazer um script que gera outro csv com os 
# dois valores separados em colunas diferentes

origem = open('arquivo.csv', 'r')
destino = open('destino.csv', 'a')

linhas = list(origem)
cabecalho = linhas[0].strip() + ";Coluna2\n"
destino.write(cabecalho)

for linha in linhas[1:]:
    colunas = linha.split(';')
    ultima_coluna = colunas[-1]
    del colunas[-1]

    valores = ultima_coluna.split(',')
    colunas = colunas + valores
    destino.write( ";".join(colunas).strip() + "\n")

origem.close()
destino.close()

print("fim")
