from dataclasses import dataclass
from enum import Enum, auto
from typing import Any


class TokenType(Enum):
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()

    MINUS = auto()
    PLUS = auto()

    NUMBER = auto()
    IDENTIFIER = auto()

    LIST = auto()
    FIRST = auto()


@dataclass(frozen=True)
class Token:
    type: TokenType
    lexeme: str
    literal: Any


class Tokenizer:
    def __init__(self, source: str):
        self.source = source
        self.tokens: list[Token] = []

        self.start_offset = 0
        self.current_offset = 0

        self.keywords = {
            "list": TokenType.LIST,
            "first": TokenType.FIRST,
        }

    def scan(self) -> list[Token]:
        while not self._is_finished():
            self.start_offset = self.current_offset
            self._scan_token()

        return self.tokens

    def _peek(self) -> str | None:
        if self._is_finished():
            return None

        return self.source[self.current_offset]

    def _advance(self) -> str:
        self.current_offset += 1

        return self.source[self.current_offset - 1]

    def _scan_token(self):
        char = self._advance()
        match char:
            case "(":
                self._add_token(TokenType.LEFT_PAREN)
            case ")":
                self._add_token(TokenType.RIGHT_PAREN)
            case "-":
                self._add_token(TokenType.MINUS)
            case "+":
                self._add_token(TokenType.PLUS)
            case _ if char.isdigit():
                self._add_number()
            case _ if char.isalpha():
                self._add_identifier()
            case " ":
                pass
            case _:
                raise Exception(f"{char=} is not supported yet!")

    def _add_token(self, token_type: TokenType, *, literal: Any = None):
        text = self.source[self.start_offset : self.current_offset]
        new_token = Token(type=token_type, lexeme=text, literal=literal)

        self.tokens.append(new_token)

    def _add_number(self):
        while (next_char := self._peek()) and next_char.isdigit():
            self._advance()

        literal = int(self.source[self.start_offset : self.current_offset])

        self._add_token(TokenType.NUMBER, literal=literal)

    def _add_identifier(self):
        while (next_char := self._peek()) and next_char.isalnum():
            self._advance()

        text = self.source[self.start_offset : self.current_offset]
        token_type = self.keywords.get(text, TokenType.IDENTIFIER)

        self._add_token(token_type)

    def _is_finished(self) -> bool:
        return self.current_offset >= len(self.source)
