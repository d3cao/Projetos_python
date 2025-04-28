#pegando infos
#primeiro dia :
dia_inicio = int(input().split()[1])
hh, mm, ss = map(int, input().split(':'))

#ultimo dia : 
dia_termino = int(input().split()[1])
h, m, s = map(int, input().split(':'))

#tempo total
inicio = (dia_inicio*86400) + (hh*3600) + (mm*60) + ss
fim = (dia_termino*86400) + (h*3600) + (m*60) + s
total = fim - inicio

print(f'{total//86400} dia(s)')
total %= 86400
print(f'{total//3600} hora(s)')
total %= 3600
print(f'{total//60} minuto(s)')
total %= 60
print(f'{total} segundo(s)')