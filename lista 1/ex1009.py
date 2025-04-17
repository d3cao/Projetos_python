nome_funcionario = input()
salario_fixo = float(input())
vendas_mes = float(input())
comissao = vendas_mes*0.15
total = salario_fixo + comissao
print(f'TOTAL = R$ {total:.2f}')