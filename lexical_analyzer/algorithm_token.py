from enum import Enum

class AlgToken(Enum):
    NUMBER = 0
    ADD = 1      # +
    MINUS = 2    # - 
    MULTIPLY = 3 # *
    DIVISION = 4 # /

    RBRACE = 5   # )
    LBRACE = 6   # (

    EQUALS = 7 # =
    GTHAN = 8 # >
    LTHAN = 9 # <

    STRING = 10

    EOF = 11      # end of expression

class AlgTokens():
    def __init__(self, tokenType, value):
        self.tokenType: AlgToken = tokenType
        self.value = value

    def toString(self):
        return " " + str(self.tokenType) + ":" + str(self.value)

