import unittest
from algorithm_lexer import AlgLexer

class TestAlgLexer(unittest.TestCase):
    def test_all_numeric_tokens(self):
        expected = "AlgToken.NUMBER:25.0 AlgToken.DIVISION:None AlgToken.LBRACE:None AlgToken.NUMBER:13.0 AlgToken.ADD:None AlgToken.NUMBER:14.0 AlgToken.RBRACE:None AlgToken.EOF:None"
        lexer = AlgLexer("25 / ( 13 + 14 )")
        tokens = lexer.getTokens()
        actual = lexer.ToString()
        self.assertIsNotNone(tokens)        
        self.assertEqual(expected, actual)

    def test_string_tokens(self):
        expected = "AlgToken.STRING:m AlgToken.STRING:a AlgToken.STRING:t AlgToken.STRING:e AlgToken.STRING:u AlgToken.STRING:s AlgToken.STRING:c AlgToken.STRING:a AlgToken.STRING:s AlgToken.STRING:t AlgToken.STRING:r AlgToken.STRING:o AlgToken.EOF:None"
        lexer = AlgLexer("mateus castro")
        tokens = lexer.getTokens()
        actual = lexer.ToString()
        self.assertIsNotNone(tokens)        
        self.assertEqual(expected, actual)

    def test_invalid_characters(self):
        self.assertRaises(Exception, AlgLexer("!@#!&¨@#"))

    def test_invalid_decimal_number(self):
        self.assertRaises(Exception, AlgLexer("2.233.4534"))
if __name__ == '__main__':
    unittest.main()