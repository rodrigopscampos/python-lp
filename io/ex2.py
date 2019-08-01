#Faça um programa que lê um arquivo e 
# gera outro invertido (a primeira linha é a última)

origem = open('origem.txt', 'r')
invertido = open('invertido.txt', 'a')

linhas = list(origem)
linhas.reverse()

for l in linhas:
    invertido.write(l.strip() + "\n")
    
origem.close()
invertido.close()