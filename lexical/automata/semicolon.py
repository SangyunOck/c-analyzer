from lexical.dfa import DFA

class Semicolon(DFA):
    states = {
        "t0": {";": "t1"}
    }
    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return True, self.value
        except KeyError:
            return False, None
    