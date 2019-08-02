# Peça um número para o usuário e calcule a tabuada de 0 até 10

n = int(input("Informe um número: "))
saida = [(n, i, n*i) for i in range(0, 11)]

for a, b, c in saida:
    print("{} X {} = {}".format(a, b, c))
