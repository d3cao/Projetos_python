entradas = int(input())

def mdc(a, b):
    while b :
        a, b = b, a % b
    return a

operacoes = {
    '+' : lambda n1, n2, d1, d2 : (n1 * d2 + n2 * d1, d1 * d2),
    '-' : lambda n1, n2, d1, d2 : (n1 * d2 - n2 * d1, d1 * d2), 
    '*' : lambda n1, n2, d1, d2 : (n1 * n2, d1 * d2),
    '/' : lambda n1, n2, d1, d2 : (n1 * d2, d1 * n2)
}

for _ in range(entradas):
    valor = list(input().split())

    n1, d1, n2, d2  = int(valor[0]), int(valor[2]), int(valor[4]), int(valor[6])

    num, num1 = operacoes.get(valor[3])(n1, n2, d1, d2)
    divisor = mdc(abs(num), abs(num1))
    print(f'{num}/{num1} = {num//divisor}/{num1//divisor}')