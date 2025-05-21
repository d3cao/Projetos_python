fib = [0,1]

for i in range(60):
    valor = fib[i] + fib[i+1]
    fib.append(valor)

num_casos = int(input())

for i in range(num_casos):
    enesimo_fb = int(input())
    print(f'Fib({enesimo_fb}) = {fib[enesimo_fb]}')