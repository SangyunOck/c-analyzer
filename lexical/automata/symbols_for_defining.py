from lexical.dfa import DFA

class SymbolsForDenifing(DFA):
    stats = {
        "t0": {"{", "t1", "}", "t1"}
    }
    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, self.value
        except KeyError:
            return False, None