n = int(input())
c = 0

while c < n :
    n1,n2 = map(int, input().strip().split())

    if n2 == 0 :
        print('divisao impossivel')
    else :
        print(f'{n1/n2:.1f}')
    
    c += 1