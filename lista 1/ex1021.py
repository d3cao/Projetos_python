valor = float(input())

def calcular_qnt_notas(valor, num) :
    notas = valor // num
    valor = valor - (notas*num)
    if num == 1 :
        print(f'{int(notas)} moeda(s) de R$ {num}.00')
    else :
        print(f'{int(notas)} nota(s) de R$ {num}.00')
    return valor

print('NOTAS:')
valor = calcular_qnt_notas(valor, 100)
valor = calcular_qnt_notas(valor, 50)
valor = calcular_qnt_notas(valor, 20)
valor = calcular_qnt_notas(valor, 10)
valor = calcular_qnt_notas(valor, 5)
valor = calcular_qnt_notas(valor, 2)

def calcular_qnt_moedas(valor, num) :
    notas = valor // num
    valor = valor - (notas*num)
    print(f'{int(notas)} moeda(s) de R$ {num:.2f}')
    return valor

print('MOEDAS:')
valor = calcular_qnt_moedas(valor, 1)
valor = calcular_qnt_moedas(valor, 0.50)
valor = calcular_qnt_moedas(valor, 0.25)
valor = calcular_qnt_moedas(valor, 0.10)
valor = calcular_qnt_moedas(valor, 0.05)
print(f'{(valor/0.01):.0f} moeda(s) de R$ 0.01')