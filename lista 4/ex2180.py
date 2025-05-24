combustivel = int(input())
lista = []
seq = combustivel + 1

def num_primo(num) :
    for i in range(2, int(num**0.5)+1) :
        if num < 2 :
            return False
        elif num%i == 0 :
            return False
    return True

if num_primo(combustivel) :
    lista.append(combustivel)
    while len(lista) < 10 :
        if num_primo(seq) :
            lista.append(seq)
        seq += 1

else :
    while len(lista) < 10 :
        if num_primo(seq) :
            lista.append(seq)
        seq += 1

soma = sum(lista)
temp = 60000000//soma
print(f'{soma} km/h')
print(f'{temp} h / {temp//24} d')