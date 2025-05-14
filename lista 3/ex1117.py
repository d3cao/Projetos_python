c = 0
notas = []

while c < 2:
    nota = float(input()) 
    if nota >= 1 and nota <= 10 :
        notas.append(nota)
        c += 1
    else :
        print('nota invalida')

    if len(notas) == 2:
        media = (notas[0] + notas[1])/2

print(f'media = {media}')