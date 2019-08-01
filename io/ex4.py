# Faça um programa que remove todos os
# espaços de um arquivo e gere outro

origem = open('origem.txt', 'r')
destino = open('destino.txt', 'a')

for linha in origem:
    destino.write(linha.replace(" ", ""))
