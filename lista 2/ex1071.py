num1 = int(input())
num2 = int(input())
soma = 0

if num1 < num2 :
    for i in range(num1-1, num2):
        if i%2 != 0 :
            soma = soma + i
else :
    for i in range(num2+1, num1):
        if i%2 != 0 :
            soma = soma + i

print(soma)