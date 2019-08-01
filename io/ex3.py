#Faça um programa que lê um arquivo e 
# gere outro igual, mas com todo o texto em 
# minúsculo ou maiúsculo, de acordo com a opção 
# do usuário.

origem = open('origem.txt', 'r')
destino = open('destino.txt', 'w')

maiusculo = True

for linha in origem:
    if maiusculo:
        destino.write(linha.upper())
    else:
        destino.write(linha.lower())
