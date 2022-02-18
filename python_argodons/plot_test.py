
def teste_while(str, charNum):
    lala=True
    i=0
    l=0
    while lala:
        if(l >= len(str)):
            lala=False

        if(i==charNum):
            i=0
            l+=1

        print(f'{str[0:l]}{chr(i)}{str[l+1:len(str)]}')
        i+=1

    print(f'parabens voce acaba de ver {l*charNum} formas de escrever "{str}" :D')

teste_while('vo mija',55294)
    