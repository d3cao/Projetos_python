x = float(input())
vetor = []
vetor.append(x)
for i in range(99):
    num = vetor[i]/2
    vetor.append(num)

for i in range(len(vetor)):
    print(f'N[{i}] = {vetor[i]:.4f}')