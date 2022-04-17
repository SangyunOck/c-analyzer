from lexical.dfa import (
    ALPHABET_LOWER,
    ALPHABET_UPPER,
    DFA,
    DIGIT,
    WHITESPACE,
    LexicalError,
)

alphabet_lower = ALPHABET_LOWER
alphabet_upper = ALPHABET_UPPER
digits = DIGIT
whitespace = WHITESPACE


class LiteralString(DFA):

    states = {}
    states["t0"] = {'"': "t1"}
    states["t1"] = {i: "t2" for i in digits}
    for i in alphabet_lower + alphabet_upper:
        states["t1"][i] = "t3"
    for i in whitespace:
        states["t1"][i] = "t4"

    states["t2"] = {'"': "t5"}
    for i in digits:
        states["t2"][i] = "t6"
    for i in alphabet_lower + alphabet_upper:
        states["t2"][i] = "t7"
    for i in whitespace:
        states["t2"][i] = "t8"

    states["t3"] = {'"': "t5"}
    for i in digits:
        states["t3"][i] = "t6"
    for i in alphabet_lower + alphabet_upper:
        states["t3"][i] = "t7"
    for i in whitespace:
        states["t3"][i] = "t8"

    states["t4"] = {'"': "t5"}
    for i in digits:
        states["t4"][i] = "t6"
    for i in alphabet_lower + alphabet_upper:
        states["t4"][i] = "t7"
    for i in whitespace:
        states["t4"][i] = "t8"

    states["t6"] = {'"': "t5"}
    for i in digits:
        states["t6"][i] = "t6"
    for i in alphabet_lower + alphabet_upper:
        states["t6"][i] = "t7"
    for i in whitespace:
        states["t6"][i] = "t8"

    states["t7"] = {'"': "t5"}
    for i in digits:
        states["t7"][i] = "t6"
    for i in alphabet_lower + alphabet_upper:
        states["t7"][i] = "t7"
    for i in whitespace:
        states["t7"][i] = "t8"

    states["t8"] = {'"': "t5"}
    for i in digits:
        states["t8"][i] = "t6"
    for i in alphabet_lower + alphabet_upper:
        states["t8"][i] = "t7"
    for i in whitespace:
        states["t8"][i] = "t8"

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            if self.state == "t5":
                return True, self.value
        except KeyError:
            if self.state != "t5":
                raise LexicalError('Needed ", line', line_num)
