#Recebe o valor
valor = int(input())

def calcular_qnt_notas(valor, num) :
    notas = valor // num
    valor = valor - (notas*num)
    print(f'{notas} nota(s) de R$ {num},00')
    return valor

print(valor)
valor = calcular_qnt_notas(valor, 100)
valor = calcular_qnt_notas(valor, 50)
valor = calcular_qnt_notas(valor, 20)
valor = calcular_qnt_notas(valor, 10)
valor = calcular_qnt_notas(valor, 5)
valor = calcular_qnt_notas(valor, 2)
valor = calcular_qnt_notas(valor, 1)