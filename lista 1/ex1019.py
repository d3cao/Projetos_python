valor = int(input())
horas = valor//3600
valor = valor - horas*3600
minutos = valor//60
valor = valor - minutos*60
print(f'{horas}:{minutos}:{valor}')