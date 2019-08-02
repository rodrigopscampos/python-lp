# A ultima coluna do arquivo.csv (Selecione Tipo de CE Simp 4)
# possui dois números separados por vírgula
# O desafio é fazer um script que gera outro csv com os 
# dois valores separados em colunas diferentes
# Além disso, o conteúdo da coluna "Subsistema" é igual em todas as linhas
# por isto, o arquivo de saída não deve conter esta coluna

origem = open('arquivo.csv', 'r')
destino = open('destino.csv', 'w')

linhas = list(origem)
cabecalho = linhas[0].strip()
colunas_cabecalho = cabecalho.split(';')
del colunas_cabecalho[3]
colunas_cabecalho.append("Coluna Extra")
destino.write( ";".join(colunas_cabecalho).strip() + "\n" )

for linha in linhas[1:]:
    colunas = linha.split(';')
    ultima_coluna = colunas[-1]
    del colunas[3]
    del colunas[-1]

    valores = ultima_coluna.split(',')
    colunas = colunas + valores
    destino.write( ";".join(colunas).strip() + "\n")

origem.close()
destino.close()

print("fim")
