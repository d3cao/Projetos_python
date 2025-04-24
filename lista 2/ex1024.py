entrada_usuario = list('Texto #3')
tamanho = len(entrada_usuario)

def primeira_passada():
    for i, caracter in enumerate(entrada_usuario) :
        if caracter.isalpha() :
            entrada_usuario[i] = chr(ord(caracter)+3)
    #print(entrada_usuario)

def reverse(lista):
    i = 1
    listar = []
    while i <= len(lista):
        listar.append(lista[len(lista)-i])
        i += 1
    return listar       

def segunda_passada():
    reverse(entrada_usuario)
    print(entrada_usuario)


primeira_passada()
segunda_passada()