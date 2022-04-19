from lexical.dfa import DFA
from lexical.dfa import LexicalError

class WhiteSpace(DFA):
    states = {
        "t0": {"\\": "t1"},
        "t1": {"t": "t2", "n": "t3", "0": "t4"},
        "t2": {"\\": "t5"},
        "t3": {"\\": "t5"},
        "t4": {"\\": "t5"},
        "t5": {"t": "t6", "n": "t7", "0": "t8"},
        "t6": {"\\": "t5"},
        "t7": {"\\" "t5"},
        "t8": {"\\": "t5"}  
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return True, None, None
        except KeyError:
            if self.state in ["t2", "t3", "t4", "t6", "t7", "t8"]:
                returnVal = self.value
                self.reset()
                return False, "WHITESPACE", returnVal
            if self.state in ["t1", "t5"]:
                raise LexicalError("t, n, 0 have to come after '\'", line_num)
            else:
                return False, None, None