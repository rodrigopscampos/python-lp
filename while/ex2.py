#Solicite usuário e senha até que a o usuário seja “python” e senha “python132”

while True:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == "python" and senha == "python132":
        break

    print('Usuário ou senha inválido, tente novamente.')

print('Bem-Vindo :D')