n1, n2, n3, n4 = map(int, input().strip().split())

#triangulos : n1, n2, n3; n2, n3, n4; n1, n3, n4;

def teste_triangulo(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else :
        return False

if teste_triangulo(n1, n2, n3) or teste_triangulo(n2, n3, n4) or teste_triangulo(n1, n3, n4) or teste_triangulo(n1, n2, n4):
    print('S')
else :
    print('N')