num, num2 = map(int, input().strip().split())

if num&num2 == 0 or num2%num == 0:
    print('Sao Multiplos')
    
else :
    print('Nao sao Multiplos')