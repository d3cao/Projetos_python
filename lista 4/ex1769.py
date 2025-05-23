while True :
    try :
        entrada = input().strip()
        cpf = []
        for letra in entrada:
            if letra.isnumeric():
                cpf.append(letra)

        def verify_b1cpf(cpf):
            soma = 0
            for i in range(9):
                soma = soma + (int(cpf[i])*(i+1))
            divisao = 0 if soma%11 == 10 else soma%11
            if divisao == int(cpf[9]):
                return True
            else :
                return False

        def verify_b2cpf(cpf):
            soma = 0
            for i in range(9):
                soma = soma + (int(cpf[i])*(9-i))
            divisao = 0 if soma%11 == 10 else soma%11
            if divisao == int(cpf[10]):
                return True
            else :
                return False

        if verify_b1cpf(cpf) and verify_b2cpf(cpf):
            print('CPF valido')
        else :
            print('CPF invalido')
    
    except EOFError:
        break