while True:
    try:
        def cria_matriz(num):
            matriz = [[0]*num for _ in range(num)]
            centro = num//2
            ref = num//3

            for i in range(num):
                matriz[i][(num-1)-i] = 3


            for i in range(num):
                for j in range(num):
                    if i == j :
                        matriz[i][j] = 2

            for i in range(ref, num - ref):
                for j in range(ref, num - ref):
                    matriz[i][j] = 1
            matriz[centro][centro] = 4

            return matriz

        while True :
            n = int(input())
            if n == 0 :
                break
            else :
                matriz = cria_matriz(n)
                tam = len(str(matriz[n-1][n-1]))
                for linha in matriz :
                    print(''.join(f'{str(item)}' for item in linha))
                print()

    except EOFError :
        break