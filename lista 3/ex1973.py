n = int(input())
fazendas = list(map(int, input().strip().split()))
prox_fazenda = 0
carneiros = sum(fazendas)
num_fazendas = 0

for i in range(n):
    if prox_fazenda == 0 :
        break
    elif prox_fazenda > n :
        break
    else :
        carneiros -= 1
        num_fazendas += 1
        if fazendas[i]%2 == 0 :
            prox_fazenda -= 1
        else :
            prox_fazenda += 1

print(f'{num_fazendas} {carneiros}')