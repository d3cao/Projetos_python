matriz = []
soma = 0
media = 0

#Linha da operação + operação a ser feita
linha = int(input())
oper = input().strip().lower()

#gera a matriz em uma lista

for i in range(144) :
    a = float(input())
    matriz.append(a)

#determina a linha

a = 12*linha
teste = []
for i in range(a, a+12):
    teste.append(matriz[i])

#realiza a soma

for i in range(len(teste)) :
        soma = soma + float(teste[i])

#Realiza a media

media = soma/12

#imprime o resultado pedido

if oper == 's' :
    print(f'{soma:.1f}')
elif oper == 'm':
    print(f'{media:.1f}')