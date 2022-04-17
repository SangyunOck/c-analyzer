WHITESPACE = [" ", "\t", "\0", "\n"]
OPERATOR = ["+", "-", "*", "/"]
PROGRAM_KEYWORD = [",", ";"]


class DFA:
    state = "t0"
    value = ""

    def reset(self):
        self.state = "t0"
        self.value = ""


class LexicalError(Exception):
    def __init__(self, msg, line_num) -> None:
        self.msg = f"{msg}, line {line_num}"

    def __str__(self) -> str:
        return self.msg
