import math
#Recebe os valores
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
#trata os valores comparando eles
maior1 = (a+b+abs(a-b))/2
maior2 = (maior1+c+abs(maior1-c))/2
print(f'{int(maior2)} eh o maior')