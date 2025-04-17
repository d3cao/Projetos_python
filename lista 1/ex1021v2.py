valor = float(input())

notas=[100,50,20,10,5,2]
moedas=[1,0.50,0.25,0.10,0.05,0.01]

if valor > 2:
   print('NOTAS:')
   for nota in notas:
       qtd = valor // nota
       valor = valor - (qtd * nota)
       print(f'{int(qtd)} nota(s) de R$ {nota:.2f}')
   else:
       print('MOEDAS:')
       for moeda in moedas:
           qtd = valor // moeda
           valor = valor - (qtd * moeda)
           print(f'{int(qtd)} moeda(s) de R$ {moeda:.2f}')
print('')           
        
