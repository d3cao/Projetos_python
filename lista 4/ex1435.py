def cria_matriz(num):
    matriz = [[0]*num for _ in range(num)]
    camadas = (num + 1)//2
    for camada in range(camadas):
        valor = camada+1
        for i in range(camada, num - camada):
            for j in range(camada, num - camada):
                matriz[i][j] = valor
    return matriz

while True :
    n = int(input())
    if n == 0 :
        break
    else :
        matriz = cria_matriz(n)
        for linha in matriz :
            print(' '.join(f'{item:3}' for item in linha))
        print()