p, j1, j2, r, a = map(int, input().strip().split())

soma = j1 + j2
escolha = True if p == 1 else False
par = True if soma%2 == 0 else False
roubo = True if r == 1 else False
acusar = True if a == 1 else False

if roubo == True and acusar == True:
    print('Jogador 2 ganha!')
elif roubo == True and acusar == False :
    print('Jogador 1 ganha!')
else :
    if par == True and escolha == True :
        print('Jogador 1 ganha!')
    elif par == False and escolha == False :
        print('Jogador 1 ganha!')
    else :
        print('Jogador 2 ganha!')