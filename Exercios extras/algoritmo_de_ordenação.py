n = [int(num) for num in input().split()]

def ordenacao(lista) :
    for i in range(len(lista)) :
        for j in range(i+1, len(lista)) :
            if lista[i] > lista[j] :
                lista[i], lista[j] = lista[j], lista[i]
    return lista

lista_ordenada = ordenacao(n)

print(' '.join(str(i) for i in lista_ordenada))