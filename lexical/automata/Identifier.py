from lexical.dfa import ALPHABET_LOWER, ALPHABET_UPPER, DFA, DIGIT


class Identifier(DFA):
    states = {
        "t0": {i: "t1" for i in ALPHABET_LOWER + ALPHABET_UPPER},
        "t1": {i: "t2" for i in ALPHABET_LOWER + ALPHABET_UPPER},
        "t2": {i: "t2" for i in ALPHABET_LOWER + ALPHABET_UPPER},
        "t3": {i: "t2" for i in ALPHABET_LOWER + ALPHABET_UPPER},
    }
    for i in DIGIT:
        states["t1"][i] = "t3"
        states["t2"][i] = "t3"
    for i in ALPHABET_LOWER + ALPHABET_UPPER:
        states["t3"][i] = "t3"

    def accept(self, i) -> None:
        try:
            super().accept(i)
            return False, None, None
        except KeyError:
            if self.state in ["t1", "t2", "t3"]:
                return True, "IDENTIFIER", self.value
