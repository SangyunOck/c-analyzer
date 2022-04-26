import string
from enum import Enum

WHITESPACE = [" ", "\t", "\0", "\n"]
ARITHMATIC_OPERATOR = ["+", "-", "*", "/"]
PROGRAM_KEYWORD = [",", ";", "="]
NON_ZERO_DIGIT = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
DIGIT = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL_CHARS = [
    "@",
    "#",
    "$",
]
ALPHABET_LOWER = list(string.ascii_lowercase)
ALPHABET_UPPER = list(string.ascii_uppercase)

# transition state를 담고 있는 enum class
# FAIL: transition 실패
# SUCCESS: transition성공, final state에 도달하지는 못함
# COMPLETE: transition실패, final state에 도달
class TransitionState(Enum):
    FAIL = 0
    SUCCESS = 1
    COMPLETE = 3

# 모든 오토마타의 Parent Class로, 오토마타의 behavior을 정의함
# t_new = q(t_old, i)의 형태로 block되지 않으면 accept가 진행.

class DFA:
    state = "t0"
    value = ""
    is_blocked = False
    states = {}

    def reset(self):
        self.state = "t0"
        self.value = ""
        self.is_blocked = False

    # line_num은 추후 syntactic anlyzer에서 error handling을 위해 사용
    def accept(self, i, line_num):
        if not self.is_blocked:
            self.state = self.states[self.state][i]
            self.value += i

    def block(self):
        self.is_blocked = True

    def unblock(self):
        self.is_blocked = False

# lexical 에러가 발생하면 raise되는 exception클래스. 에러 메시지 + 라인번호의 형태
class LexicalError(Exception):
    def __init__(self, msg, line_num):
        self.msg = f"{msg}, line {line_num}"

    def __str__(self) -> str:
        return self.msg
