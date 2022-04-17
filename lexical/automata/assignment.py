from lexical.dfa import DFA


class Assignment(DFA):
    states = {"t0": {"=": "t1"}}

    def accept(self, i, line_num):
        try:
            super().accept(i)
            returnVal = self.value
            self.reset()
            return True, "ASSIGNMENT", returnVal
        except KeyError:
            self.reset()
            return None, None, None
