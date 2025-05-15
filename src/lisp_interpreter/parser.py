from typing import Iterator

from lisp_interpreter.tokenizer import Token, TokenType


def parse_ast(tokens: Iterator[Token]) -> list[list[Token] | Token]:
    ast = []

    for token in tokens:
        match token.type:
            case TokenType.LEFT_PAREN:
                ast.append(parse_ast(tokens))
            case TokenType.RIGHT_PAREN:
                return ast
            case _:
                ast.append(token)

    return ast
