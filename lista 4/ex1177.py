seq = int(input())
vetor = []
control = 0
while len(vetor) < 1000 :
    if control == seq :
        control = 0
    else :
        vetor.append(control)
        control += 1

for i in range(len(vetor)):
    print(f'N[{i}] = {vetor[i]}')