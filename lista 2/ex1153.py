n = int(input())
a = n
for i in range(n) :
    if i > 0 :
        a = a*(n-i)
print(a)