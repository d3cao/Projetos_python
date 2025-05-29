entrada = int(input())

def mdc(a, b):
    while b:
        a, b = b, a%b
    return a

for i in range(entrada):
    p1, p2 = map(int, input().strip().split())
    print(mdc(p1, p2))