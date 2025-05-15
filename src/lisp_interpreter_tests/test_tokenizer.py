from lisp_interpreter.tokenizer import Token, Tokenizer, TokenType


def test_tokenizer():
    source = "(first (list 1 (+ 2 3) 9))"
    tokens = Tokenizer(source).scan()

    assert tokens == [
        Token(TokenType.LEFT_PAREN, "(", None),
        Token(TokenType.FIRST, "first", None),
        Token(TokenType.LEFT_PAREN, "(", None),
        Token(TokenType.LIST, "list", None),
        Token(TokenType.NUMBER, "1", 1),
        Token(TokenType.LEFT_PAREN, "(", None),
        Token(TokenType.PLUS, "+", None),
        Token(TokenType.NUMBER, "2", 2),
        Token(TokenType.NUMBER, "3", 3),
        Token(TokenType.RIGHT_PAREN, ")", None),
        Token(TokenType.NUMBER, "9", 9),
        Token(TokenType.RIGHT_PAREN, ")", None),
        Token(TokenType.RIGHT_PAREN, ")", None),
    ]
