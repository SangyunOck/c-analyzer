from lexical.dfa import DFA

class Comparision(DFA):
    states = {
        "t0": {"<": "t1"},
        "t0": {">": "t2"},
        "t0": {"==", "t3"},
        "t0": {"!=", "t4"},
        "t0": {"<=", "t5"},
        "t0": {">=", "t6"}
    }
    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return True, self.value
        except KeyError:
            return False, None
        