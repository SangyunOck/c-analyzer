from lexical.dfa import DFA


class SymbolsForDefining(DFA):
    stats = {"t0": {"{", "t1", "}", "t1"}}

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return True, "SYMBOLSFORDEFINING", self.value
        except KeyError:
            return False, None, None
