import string

WHITESPACE = [" ", "\t", "\0", "\n"]
OPERATOR = ["+", "-", "*", "/"]
PROGRAM_KEYWORD = [",", ";"]
NON_ZERO_DIGIT = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ALPHABET_LOWER = list(string.ascii_lowercase)
ALPHABET_UPPER = list(string.ascii_uppercase)


class DFA:
    state = "t0"
    value = ""
    states = {}

    def reset(self):
        self.state = "t0"
        self.value = ""

    def accept(self, i) -> None:
        self.state = self.states[self.state][i]
        self.value += i


class LexicalError(Exception):
    def __init__(self, msg, line_num) -> None:
        self.msg = f"{msg}, line {line_num}"

    def __str__(self) -> str:
        return self.msg
