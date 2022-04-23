from lexical.dfa import (
    ALPHABET_LOWER,
    ALPHABET_UPPER,
    DFA,
    DIGIT,
    WHITESPACE,
    LexicalError,
    TransitionState,
)

digits = DIGIT
whitespace = WHITESPACE
letters = ALPHABET_LOWER + ALPHABET_UPPER


class LiteralString(DFA):

    states = {
        "t0": {'"': "t1"},
        "t1": {i: "t1" for i in letters + digits + whitespace},
    }
    states["t1"]['"'] = "t2"
    

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t1":
                raise LexicalError('Need " to complete string', line_num)
            if self.state == "t2":
                return TransitionState.COMPLETE, "LITERALSTRING", self.value
            else:
                return TransitionState.FAIL, None, None
