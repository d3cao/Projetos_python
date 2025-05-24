num, num1 = map(int, input().split())
matriz = [[0]*num1 for _ in range(num)]
Assou = False
coordenadas = [0, 0]

for i in range(num):
    entrada = input().split()
    for j in range(num1):
        matriz[i][j] = entrada[j]

for i in range(1, num-1):
    for j in range(1, num1-1):
        if matriz[i][j] == '42':
            if matriz[i-1][j] == '7' and matriz[i-1][j-1] == '7' and matriz[i-1][j+1] == '7':
                if matriz[i+1][j] == '7' and matriz[i+1][j-1] == '7' and matriz[i+1][j+1] == '7':
                    if matriz[i][j-1] == '7' and matriz[i][j+1] == '7':
                        Assou = True
                        coordenadas[0] = i + 1
                        coordenadas[1] = j + 1
                        break
    if Assou:
        break
if Assou:
    print(coordenadas[0], coordenadas[1])
else:
    print('0 0')