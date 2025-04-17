#Input do usuário
num_funcionario = int(input())
horas_trabalhadas = int(input())
hora_salario = float(input())
#calculo e print do salario
salario = hora_salario*horas_trabalhadas
print(f'NUMBER = {num_funcionario}')
print(f'SALARY = U$ {salario:.2f}')