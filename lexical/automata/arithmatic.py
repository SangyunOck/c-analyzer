from lexical.dfa import DFA


class Arithmatic(DFA):
    states = {"t0": {"+": "t1", "-": "t2", "*": "t3", "/": "t4"}}

    def accept(self, i, line_num):
        try:
            super().accept(i)
            return True, None, None
        except KeyError:
            if self.state in ["t1", "t2", "t3", "t4"]:
                returnVal = self.value
                self.reset()
                return False, "ARITHMATIC", returnVal
            else:
                return False, None, None
