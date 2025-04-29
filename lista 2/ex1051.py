salary = float(input())
total = 0

if 2000.01 <= salary <= 3000.00 :
    total = (salary - 2000.00)*0.08
    print(f'R$ {total:.2f}')
elif  3000.01 <= salary <= 4500.00 :
    tax_a = 1000*0.08
    total = (salary - 3000.00)*0.18 + tax_a
    print(f'R$ {total:.2f}')
elif salary > 4500.00 :
    tax_a = 1000*0.08
    tax_b = 1500*0.18
    total = (salary - 4500.00)*0.28 + tax_a + tax_b
    print(f'R$ {total:.2f}')
else :
    print('Isento')