def imprime_linha(num, num1, num2):
    if len(num) == 1 and len(num1) == 1:
        print('|'+' '*6+num+' '*4+'|'+' '*4+num1+' '*4+'|'+' '*7+num2+' '*7+'|')
    elif len(num) == 1 and len(num1) == 2:
        print('|'+' '*6+num+' '*4+'|'+' '*3+num1+' '*4+'|'+' '*7+num2+' '*7+'|')
    elif len(num) == 2 and len(num1) == 2:
        print('|'+' '*5+num+' '*4+'|'+' '*3+num1+' '*4+'|'+' '*7+num2+' '*7+'|')


print('-'*39)
print('|'+' '*2+'decimal'+' '*2+'|'+' '*2+'octal'+' '*2+'|'+' '*2+'Hexadecimal'+' '*2+'|')
print('-'*39)
imprime_linha('0', '0', '0')
imprime_linha('1', '1', '1')
imprime_linha('2', '2', '2')
imprime_linha('3', '3', '3')
imprime_linha('4', '4', '4')
imprime_linha('5', '5', '5')
imprime_linha('6', '6', '6')
imprime_linha('7', '7', '7')
imprime_linha('8', '10', '8')
imprime_linha('9', '11', '9')
imprime_linha('10', '12', 'A')
imprime_linha('11', '13', 'B')
imprime_linha('12', '14', 'C')
imprime_linha('13', '15', 'D')
imprime_linha('14', '16', 'E')
imprime_linha('15', '17', 'F')
print('-'*39)