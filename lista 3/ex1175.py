vetor = []

for i in range(20):
    n = int(input())
    vetor.append(n)

for i in range(10):
    vetor_1 = vetor[0+i]
    vetor_2 = vetor[19-i]
    vetor[0+i] = vetor_2
    vetor[19-i] = vetor_1

for i in range(20):
    print(f'N[{i}] = {vetor[i]}')