from lexical.dfa import DFA


class SymbolsForIndicating(DFA):
    states = {"t0": {"(": "t1", ")": "t1"}}

    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, "SYMBOLSFORINDICATING", self.value

        except KeyError:
            return False, None, None
