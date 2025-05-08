i = 1
j = 7 

while i <= 9:
    print(f'I={i} J={j}')
    for c in range(2):
        j -= 1
        print(f'I={i} J={j}')
    i += 2
    j += 4