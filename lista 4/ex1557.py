def cria_matriz(num):
    matriz = [[1]*num for _ in range(num)]
    for i in range(num):
        for j in range(num):
            if i != 0:
                matriz[i][0] = matriz[i-1][1]
            if j != 0:
                matriz[i][j] = matriz[i][j-1]*2
    return matriz

while True :
    n = int(input())
    if n == 0 :
        break
    else :
        matriz = cria_matriz(n)
        tam = len(str(matriz[n-1][n-1]))
        for linha in matriz :
            print(' '.join(f'{str(item).rjust(tam)}' for item in linha))
        print()