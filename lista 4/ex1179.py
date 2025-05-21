vetor_par = []
vetor_impar = []

def imprime_vetor(vetor, indice):
    for i in range(indice, len(vetor)):
        print(f'N[{i}] = {vetor[i]}')

for i in range(15):
    num = int(input())
    if num % 2 == 0 :
        vetor_par.append(num)
        if len(vetor_par) == 5 :
            for j in range(5):
                print(f'par[{j}] = {vetor_par[j]}')
            vetor_par = []
    else :
        vetor_impar.append(num)
        if len(vetor_impar) == 5 :
            for j in range(5):
                print(f'impar[{j}] = {vetor_impar[j]}')
            vetor_impar = []


for i in range(len(vetor_impar)):
    print(f'impar[{i}] = {vetor_impar[i]}')

for i in range(len(vetor_par)):
    print(f'par[{i}] = {vetor_par[i]}')