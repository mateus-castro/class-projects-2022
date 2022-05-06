from decimal import InvalidOperation
from algorithm_token import AlgToken
from algorithm_token import AlgTokens
from typing import List

class AlgLexer():
    __numberList = [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    __stringList = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    def __init__(self, input_from_user):
        self.pos: int = 0
        self.input = input_from_user
        self.tokens:List[AlgToken] = list()
        self.current_input = ""
        if len(input_from_user) < 0:
            self.current_input = "\0"
        else:
            self.current_input = input_from_user[self.pos]
            
    def get_next(self):
        if self.pos < len(self.input) - 1:
            self.pos = self.pos + 1
            self.current_input = self.input[self.pos]
        else:
            self.current_input = "\0"

    def getTokens(self):
        while True:
            if(self.current_input == " " or self.current_input == "\t"):
                self.get_next()
                continue

            elif(self.current_input in self.__stringList):
                stringToken = self.generateString()
                self.tokens.append(stringToken)

            elif(self.current_input in self.__numberList):
                numberToken = self.generateNumber()
                self.tokens.append(numberToken)

            elif(self.current_input == "+"):
                additionToken = AlgTokens(AlgToken.ADD, None)
                self.tokens.append(additionToken)

            elif(self.current_input == "-"):
                subtractionToken = AlgTokens(AlgToken.MINUS, None)
                self.tokens.append(subtractionToken)

            elif(self.current_input == "*"):
                multiplyToken = AlgTokens(AlgToken.MULTIPLY, None)
                self.tokens.append(multiplyToken)

            elif(self.current_input == "/"):
                divideToken = AlgTokens(AlgToken.DIVISION, None)
                self.tokens.append(divideToken)

            elif(self.current_input == "("):
                lbraceToken = AlgTokens(AlgToken.LBRACE, None)
                self.tokens.append(lbraceToken)

            elif(self.current_input == ")"):
                rbraceToken = AlgTokens(AlgToken.RBRACE, None)
                self.tokens.append(rbraceToken)

            elif(self.current_input == "="):
                equalsToken = AlgTokens(AlgToken.EQUALS, None)
                self.tokens.append(equalsToken)

            elif(self.current_input == ">"):
                gthanToken = AlgTokens(AlgToken.GTHAN, None)
                self.tokens.append(gthanToken)

            elif(self.current_input == "<"):
                lthanToken = AlgTokens(AlgToken.LTHAN, None)
                self.tokens.append(lthanToken)


            elif(self.current_input == "\0" or self.current_input == "\n"):
                token = AlgTokens(AlgToken.EOF, None)
                self.tokens.append(token)
                break
            
            else:
                inp = self.current_input
                message =  inp + " e um caracter inválido para o analisador"
                raise InvalidOperation(message)

            self.get_next()
        return self.tokens

    def generateNumber(self):
        decimal_count = 0
        stringList = ""

        while(self.current_input in self.__numberList):
            if self.current_input == "." and decimal_count < 1:
                decimal_count = decimal_count + 1
            if(len(stringList) < 1 and decimal_count > 0):
                stringList += "0"
            stringList += self.current_input
            self.get_next()

        val = float(stringList)
        return AlgTokens(AlgToken.NUMBER, val)
    
    def generateString(self):
        return AlgTokens(AlgToken.STRING, self.current_input)

    def ToString(self):
        token_string_list = ""
        for tk in self.tokens:
            token_string_list += tk.toString()
        return token_string_list[1:]
