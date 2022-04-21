import string
from enum import Enum

WHITESPACE = [" ", "\t", "\0", "\n"]
OPERATOR = ["+", "-", "*", "/"]
PROGRAM_KEYWORD = [",", ";"]
NON_ZERO_DIGIT = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
ALPHABET_LOWER = list(string.ascii_lowercase)
ALPHABET_UPPER = list(string.ascii_uppercase)

class TransitionState(Enum):
    FAIL = 0
    SUCCESS = 1
    COMPLETE = 3


class DFA:
    state = "t0"
    value = ""
    is_blocked = False
    states = {}

    def reset(self):
        self.state = "t0"
        self.value = ""
        self.is_blocked = False

    def accept(self, i) -> None:
        if not self.is_blocked:
            self.state = self.states[self.state][i]
            self.value += i

    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False


class LexicalError(Exception):
    def __init__(self, msg, line_num) -> None:
        self.msg = f"{msg}, line {line_num}"

    def __str__(self) -> str:
        return self.msg
