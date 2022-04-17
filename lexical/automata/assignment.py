from lexical.dfa import DFA

class Assignment(DFA):
    states = {
        "t0": {"=": "t1"}
    }
    def accept(self, i):
        try:
            super().accept(i)
            return True, self.value
        except KeyError:
            return None, None