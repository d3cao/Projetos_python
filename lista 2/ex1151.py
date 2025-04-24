vezes = int(input())
num, num1 = int(0),int(1)

while vezes > 0 :
    if vezes == 1 :
        print(num)
        break
    print(num, end=' ')
    num, num1 = num1, num+num1
    vezes-=1