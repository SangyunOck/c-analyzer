from lexical.dfa import DFA


class Comma(DFA):
    states = {"t0": {",": "t1"}}

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            returnVal = self.value
            self.reset()
            return True, "COMMA", returnVal
        except KeyError:
            self.reset()
            return False, None, None
