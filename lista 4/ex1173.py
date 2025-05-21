valor = int(input())
vetor = []
vetor.append(valor)

for i in range(9):
    add = vetor[i]*2
    vetor.append(add)

for i in range(len(vetor)):
    print(f'N[{i}] = {vetor[i]}')