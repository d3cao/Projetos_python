n1, n2, n3, n4 = map(float, input().split())
media = (n1*2+n2*3+n3*4+n4*1)/10
print(f'Media: {media:.1f}')
if media >= 7 :
    print('Aluno aprovado.')

elif 5 <= media <= 6.9 :
    print('Aluno em exame.')
    nota = float(input())
    print(f'Nota do exame: {nota:.1f}')
    media2 = (media+nota)/2

    if media2 >= 5 :
        print('Aluno aprovado.')

    else :
        print('Aluno reprovado.')
    print(f'Media final: {media2:.1f}')

else :
    print('Aluno reprovado.')