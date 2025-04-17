valor = int(input())
anos = valor//365
valor = valor - anos*365
meses = valor//30
valor = valor - meses*30
print(f'{anos} ano(s)\n{meses} mes(es)\n{valor} dia(s)')