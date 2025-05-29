def fib(n):    
    if n == 0 :
        return (1, 0)
    elif n == 1:
        return (1, 1)
    else :
        chamadas1, rest1 = fib(n-1)
        chamadas2, rest2 = fib(n-2)
        return (1 + chamadas1 + chamadas2, rest1 + rest2)

while True :
    try:
        entrada = int(input())
        valores = fib(entrada)
        print(f'fib({entrada}) = {valores[0] - 1} calls = {valores[1]}')
    except EOFError:
        break