from re import A
from lexical.dfa import DFA, TransitionState, DIGIT, ALPHABET_LOWER, ALPHABET_UPPER


class IntVariableType(DFA):
    states = {
        "t0": {"i": "t1", "I": "t2"},
        "t1": {"n": "t3"},
        "t2": {"N": "t4"},
        "t3": {"t": "t5"},
        "t4": {"T": "t5"},
    }
    for i in DIGIT, ALPHABET_LOWER, ALPHABET_UPPER:
        states["t5"] = {i : "t6"}

    def accept(self, i, line_num):
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t5":
                return TransitionState.COMPLETE, "INTVARIABLE", self.value
            else:
                return TransitionState.FAIL, None, None


class CharVariableType(DFA):
    states = {
        "t0": {"c": "t1", "C": "t2"},
        "t1": {"h": "t3"},
        "t2": {"H": "t4"},
        "t3": {"a": "t5"},
        "t4": {"A": "t6"},
        "t5": {"r": "t7"},
        "t6": {"R": "t7"},
    }
    for i in DIGIT, ALPHABET_LOWER, ALPHABET_UPPER:
        states["t7"] = {i : "t8"}

    def accept(self, i, line_num):
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t7":
                return TransitionState.COMPLETE, "CHARVARIABLE", self.value
            else:
                return TransitionState.FAIL, None, None
