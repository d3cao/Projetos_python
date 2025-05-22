def cria_matriz(num):
    matriz = [[1]*num for _ in range(num)]
    seq = [1]
    for x in range(num):
        valor = seq[x] + 1
        seq.append(valor)
    for i in range(num):
        for j in range(num):
                matriz[i][j] = abs(i-j)+1
    return matriz

while True :
    n = int(input())
    if n == 0 :
        break
    else :
        matriz = cria_matriz(n)
        tam = len(str(matriz[n-1][n-1]))
        for linha in matriz :
            print(' '.join(f'{str(item).rjust(3)}' for item in linha))
        print()