entrada = float(input())

if 75 < entrada <= 100 :
    print('Intervalo (75,100]')
elif 50 < entrada <= 75 :
    print('Intervalo (50,75]')
elif 25 < entrada <= 50 :
    print('Intervalo (25,50]')
elif 0 <= entrada <= 25 :
    print('Intervalo [0,25]')
else :
    print('Fora de intervalo')