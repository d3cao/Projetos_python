tipo_cha = input().strip()
resposta = input().strip()
num = 0
for i in range(len(resposta)):
    num += 1 if resposta[i] == tipo_cha else 0
print(num)