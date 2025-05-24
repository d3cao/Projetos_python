num_caso = 0
while True:
    try:
        num_caso += 1
        entrada = input().strip()
        entrada_1 = input().strip()
        
        num_seq = 0
        pos = 0
        i = 0

        while True:
            i = entrada_1.find(entrada, i)
            if i == -1:
                break
            num_seq += 1
            pos = i + 1
            i += 1

        print(f'Caso #{num_caso}:')
        if num_seq == 0:
            print('Nao existe subsequencia')
            print()
        else:
            print(f'Qtd.Subsequencias: {num_seq}')
            print(f'Pos: {pos}')
            print()
    except EOFError:
        break