from lexical.dfa import DFA


class Arithmatic(DFA):
    states = {"t0": {"+": "t1", "-": "t2", "*": "t3", "/": "t4"}}

    def accept(self, i, line_num):
        try:
            super().accept(i)
            self.returnVal = self.value
            self.reset()
            return True, "ARITHMATIC", self.returnVal
        except KeyError:
            self.reset()
            return False, None, None
