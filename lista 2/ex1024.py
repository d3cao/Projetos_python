entrada_usuario = input('Digite o texto para a criptografia ')
nomes = list(entrada_usuario)
tamanho = len(nomes)
after = []
print(nomes)

def criptografia() : 
    #Troca as letras 3 digitos depois
    for nome in nomes :
        if nome.isalpha() :
            switch = ord(nome)+3
            after.append(chr(switch))
        else :
            after.append(nome)
    print(after)
    #Inverte a string
    after.reverse()
    #Muda os termos da metade para frente
    indice_do_meio = len(after) // 2
    metade_mantida = after[0:indice_do_meio]
    metade_cifrada = after[indice_do_meio:]
    for caracter in metade_cifrada :
        num = ord(caracter) - 1
        switch = chr(num)
        metade_cifrada = metade_cifrada.append(switch)
    final = metade_mantida.append(metade_cifrada)
    print(final)
    concatenado = ''.join(after)
    return concatenado


print(criptografia())

