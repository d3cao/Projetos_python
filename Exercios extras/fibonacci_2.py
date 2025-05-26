n = int(input())

def fibonacci(n):
    lista = [0, 1]
    for i in range(n):
        valor = lista[i] + lista[i+1]
        lista.append(valor)
    return lista

seq = fibonacci(n)

print(' '.join(str(i) for i in seq))