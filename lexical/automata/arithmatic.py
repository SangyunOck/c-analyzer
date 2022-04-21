from lexical.dfa import DFA, TransitionState

class Arithmatic(DFA):
    states = {"t0": {"+": "t1", "-": "t2", "*": "t3", "/": "t4"}}

    def accept(self, i, line_num):
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t1", "t2", "t3", "t4"]:
                return TransitionState.COMPLETE, "ARITHMATIC", self.value
            else:
                return TransitionState.FAIL, None, None