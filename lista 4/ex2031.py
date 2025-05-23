n = int(input())

for i in range(n):
    entrada_1 = input().lower().strip()
    entrada_2 = input().lower().strip()

    if entrada_1 == 'pedra':
        if entrada_2 == 'ataque':
            print('Jogador 2 venceu')
        elif entrada_2 == 'papel':
            print('Jogador 1 venceu')
        elif entrada_2 == 'pedra':
            print('Sem ganhador')
    elif entrada_1 == 'papel':
        if entrada_2 == 'ataque':
            print('Jogador 2 venceu')
        elif entrada_2 == 'papel':
            print('Ambos venceram')
        elif entrada_2 == 'pedra':
            print('Jogador 2 venceu')
    elif entrada_1 == 'ataque': 
        if entrada_2 == 'ataque':
            print('Aniquilacao mutua')
        elif entrada_2 == 'papel':
            print('Jogador 1 venceu')
        elif entrada_2 == 'pedra':
            print('Jogador 1 venceu')