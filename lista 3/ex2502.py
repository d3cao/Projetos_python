while True:
    try :
        c_len, lines = map(int, input().strip().split())
        termo_1 = list(input())
        termo_2 = list(input())

        cifras = {}

        for i in range(c_len):
            cifras[termo_1[i].lower()] = termo_2[i].lower()
            cifras[termo_2[i].lower()] = termo_1[i].lower()

        for i in range(lines):
            frase = input()
            frase_final = ""
            for letras in frase :
                minus = letras.lower()
                if minus in cifras :
                    troca = cifras[minus]
                    if letras.isupper():
                        frase_final += troca.upper()
                    else :
                        frase_final += troca
                else :
                    frase_final += letras
            print(frase_final)
        print()
    except EOFError :
        break