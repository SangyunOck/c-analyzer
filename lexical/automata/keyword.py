from lexical.dfa import DFA, TransitionState


class IFKeyword(DFA):
    states = {"t0": {"i": "t1", "I": "t2"}, "t1": {"f": "t3"}, "t2": {"F": "t4"}}

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t3", "t4"]:
                return TransitionState.COMPLETE, "IFKEYWORD", self.value
            else:
                return TransitionState.FAIL, None, None


class ElSEKeyword(DFA):
    states = {
        "t0": {"e": "t1", "E": "t2"},
        "t1": {"l": "t3"},
        "t2": {"L": "t4"},
        "t3": {"s": "t5"},
        "t4": {"S": "t6"},
        "t5": {"e": "t7"},
        "t6": {"E": "t8"},
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t7", "t8"]:
                return TransitionState.COMPLETE, "ELSEKEYWORD", self.value
            else:
                return TransitionState.FAIL, None, None


class WHILEKeyword(DFA):
    states = {
        "t0": {"w": "t1", "W": "t2"},
        "t1": {"h": "t3"},
        "t2": {"H": "t4"},
        "t3": {"i": "t5"},
        "t4": {"I": "t6"},
        "t5": {"l": "t7"},
        "t6": {"L": "t8"},
        "t7": {"e": "t9"},
        "t8": {"E": "t10"},
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t9", "t10"]:
                return TransitionState.COMPLETE, "WHILEKEYWORD", self.value
            else:
                return TransitionState.FAIL, None, None


class RETURNKeyword(DFA):
    states = {
        "t0": {"r": "t1", "R": "t2"},
        "t1": {"e": "t3"},
        "t2": {"E": "t4"},
        "t3": {"t": "t5"},
        "t4": {"T": "t6"},
        "t5": {"u": "t7"},
        "t6": {"U": "t8"},
        "t7": {"r": "t9"},
        "t8": {"R": "t10"},
        "t9": {"n": "t11"},
        "t10": {"N": "t12"},
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t11", "t12"]:
                return TransitionState.COMPLETE, "RETURNKEYWORD", self.value
            else:
                return TransitionState.FAIL, None, None
