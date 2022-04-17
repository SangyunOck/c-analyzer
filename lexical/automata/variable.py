from lexical.dfa import DFA


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
            if self.state == "t5":
                returnVal = self.value
                self.reset()
                return True, returnVal
            else:
                return True, None
        except KeyError:
            return False, None
