n = int(input())

def num_primo(num) :
    valor = True
    for i in range(2, int(num**0.5)+1) :
        if num < 2 :
            valor = False
        elif num%i == 0 :
            valor = False
    return valor

for i in range(n): 
    entrada = int(input())
    if num_primo(entrada) :
        print(f'{entrada} eh primo')
    else :
        print(f'{entrada} nao eh primo')