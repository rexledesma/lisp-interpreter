from lisp_interpreter.parser import parse_ast
from lisp_interpreter.tokenizer import Token, Tokenizer, TokenType


def test_parse_ast():
    source = "(first (list 1 (+ 2 3) 9))"
    tokens = Tokenizer(source).scan()
    ast = parse_ast(iter(tokens))[0]

    assert ast == [
        Token(TokenType.FIRST, "first", None),
        [
            Token(TokenType.LIST, "list", None),
            Token(TokenType.NUMBER, "1", 1),
            [
                Token(TokenType.PLUS, "+", None),
                Token(TokenType.NUMBER, "2", 2),
                Token(TokenType.NUMBER, "3", 3),
            ],
            Token(TokenType.NUMBER, "9", 9),
        ],
    ]
