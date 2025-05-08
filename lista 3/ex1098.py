i = 0.0

while i <= 2.0 + 1e-9:
    for c in range(3):
        j = 1 + c + i

        i = round(i, 1)
        j = round(j, 1)

        if i.is_integer() and j.is_integer():
            print(f'I={int(i)} J={int(j)}')
        elif i.is_integer():
            print(f'I={int(i)} J={j}')
        elif j.is_integer():
            print(f'I={i:.1f} J={int(j)}')
        else:
            print(f'I={i:.1f} J={j:.1f}')

    i += 0.2