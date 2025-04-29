salary = float(input())

if 0 < salary <= 400.00 :
    a = salary + (salary*0.15)
    print(f'Novo salario: {a:.2f}')
    print(f'Reajuste ganho: {salary*0.15:.2f}')
    print('Em percentual: 15 %')
elif 400.01 <= salary <= 800.00 :
    a = salary + (salary*0.12)
    print(f'Novo salario: {a:.2f}')
    print(f'Reajuste ganho: {salary*0.12:.2f}')
    print('Em percentual: 12 %')
elif 800.01 <= salary <= 1200.00 :
    a = salary + (salary*0.10)
    print(f'Novo salario: {a:.2f}')
    print(f'Reajuste ganho: {salary*0.10:.2f}')
    print('Em percentual: 10 %')
elif 1200.01 <= salary <= 2000.00 :
    a = salary + (salary*0.07)
    print(f'Novo salario: {a:.2f}')
    print(f'Reajuste ganho: {salary*0.07:.2f}')
    print('Em percentual: 7 %')
elif  2000.00 < salary:
    a = salary + (salary*0.04)
    print(f'Novo salario: {a:.2f}')
    print(f'Reajuste ganho: {salary*0.04:.2f}')
    print('Em percentual: 4 %')