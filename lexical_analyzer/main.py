from decimal import InvalidOperation
from termcolor import colored
from algorithm_lexer import AlgLexer

def main():
    print("Digite uma expressão matemática e o algoritmo irá realizar uma análise léxica do input.")

    while True:
        inp = input("-> ")
        if(inp == "exit()"):
            print("bye")
            break
        if(inp != ""):
            try:
                lexer = AlgLexer(inp)
                lexer.getTokens()
                print(lexer.ToString())
            except InvalidOperation as e:
                print(colored(str(e), 'red')) 

main()