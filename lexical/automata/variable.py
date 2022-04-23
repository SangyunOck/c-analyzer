from lexical.dfa import DFA, TransitionState


class VariableType(DFA):
    states = {
        "t0": {"i": "t1", "I": "t2"},
        "t1": {"n": "t3"},
        "t3": {"t": "t5"},
        "t2": {"N": "t4"},
        "t4": {"T": "t5"},
    }

    def accept(self, i, line_num):
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t5":
                return TransitionState.COMPLETE, "VARIABLETYPE", self.value
            else:
                return TransitionState.FAIL, None, None
