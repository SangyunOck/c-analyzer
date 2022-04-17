from lexical.dfa import DFA

class Comma(DFA):
    states = {}
    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, self.value
        except KeyError:
            return False, None  