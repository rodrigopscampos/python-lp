#Leia um número, se < 10, criança, se < 18 adolescente, se não, adulto

a = int(input('Informe uma idade: '))

if a < 10:
    print('Criança')
elif a < 18:
    print('Adolescente')
else:
    print('Adulto')