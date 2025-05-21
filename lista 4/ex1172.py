vetor = []
for i in range(10):
    entrada = int(input())
    if entrada <= 0 :
        vetor.append(1)
    else :
        vetor.append(entrada)

for i in range(len(vetor)):
    print(f'X[{i}] = {vetor[i]}')