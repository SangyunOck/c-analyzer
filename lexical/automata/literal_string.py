from lexical.dfa import (
    ALPHABET_LOWER,
    ALPHABET_UPPER,
    DFA,
    DIGIT,
    SPECIAL_CHARS,
    WHITESPACE,
    LexicalError,
    TransitionState,
)

digits = DIGIT
whitespace = WHITESPACE
letters = ALPHABET_LOWER + ALPHABET_UPPER
special_chars = SPECIAL_CHARS


class LiteralString(DFA):

    states = {
        "t0": {'"': "t1"},
        "t1": {i: "t1" for i in letters + digits + whitespace + special_chars},
    }
    states["t1"]['"'] = "t2"

    def accept(self, i, line_num):
        try:
            super().accept(i, line_num)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t1":
                raise LexicalError('Need " to complete string', line_num)
            if self.state == "t2":
                return TransitionState.COMPLETE, "literal", self.value
            else:
                return TransitionState.FAIL, None, None
