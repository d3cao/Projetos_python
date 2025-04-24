data_inicio = input().split()
hora_inicio = input().split()
data_termino = input().split()
hora_termino = input().split()

#Calculo do tempo do evento
dias = (int(data_termino[1]) - int(data_inicio[1])) - 1
horas = int(hora_termino[0]) + (24 - int(hora_inicio[0]))
minutos = int(hora_termino[2]) + (60 - int(hora_inicio[2]))
segundos = int(hora_termino[4]) + (60 - int(hora_inicio[4]))

print('{} dia(s)'.format(dias))
print('{} hora(s)'.format(horas))
print('{} minuto(s)'.format(minutos))
print('{} segundo(s)'.format(segundos))

print(data_inicio)
