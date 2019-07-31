#Implemente um método input_int(), 
# que lê uma linha do console e converte o valor para int

def input_int(texto):
    r = input(texto)
    return int(r)

#Implemente um método e_positivo que recebe um número 
# e diz se é positivo ou não.

def e_positivo(n):
    return n >= 0

#Implemente um método somar, que soma todos os números de uma lista
def somar(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma

#Implementei um método categorizar_letras que
# recebe um texto e informa quantas vogais e quantas 
# consoantes o texto contém.

def categorizar_letras(texto):
    vogais = 0
    consoantes = 0
    for letra in texto:
        if letra in "aeiouAEIOU":
            vogais += 1
        else:
            consoantes += 1
    
    return (vogais, consoantes)

v,c = categorizar_letras("OlaMundo")

print("Qtdade de Vogais: " + str(v))
print("Qtdade de Consoantes: " + str(c))

