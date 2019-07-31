# Faça um programa que lê um arquivo e conta a quantidade de linhas

from os import listdir
from os.path import isfile, join

arquivos = [f for f in listdir(".") if isfile(join(".", f))]

for item in arquivos:
    f = open(item, 'r')
    
    # modo simples, mas que consome mais memória
    #qtd_linhas = len(list(f))

    # modo que consome menos memória
    qtd_linhas = 0
    for linha in f:
        qtd_linhas += 1
    
    print("{}: {}".format(item, qtd_linhas))
    f.close()