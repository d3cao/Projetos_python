cod1, num1, valor1 = input().split()
cod2, num2, valor2 = input().split()

item1 = float(num1) * float(valor1)
item2 = float(num2) * float(valor2)

total = item1 + item2
print(f'VALOR A PAGAR: R$ {total:.2f}')