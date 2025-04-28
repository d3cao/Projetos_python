#entrada_usuario = list('Texto #3')
linhas = int(input())

def primeira_passada():
    global entrada_usuario
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

def terceira_passada():
    global entrada_usuario
    indice_meio = len(entrada_usuario)//2
    for i in range(indice_meio, len(entrada_usuario)):
        entrada_usuario[i] = chr(ord(entrada_usuario[i])-1)
    concatenado = ''.join(entrada_usuario)
    print(concatenado)


def segunda_passada():
    global entrada_usuario
    entrada_usuario = reverse(entrada_usuario)


for i in range(linhas):
    entrada_usuario = list(input())
    tamanho = len(entrada_usuario)
    primeira_passada()
    segunda_passada()
    terceira_passada()