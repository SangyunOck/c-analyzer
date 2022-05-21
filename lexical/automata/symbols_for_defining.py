from lexical.dfa import DFA, TransitionState


class SymbolsForDefining(DFA):
    states = {
        "t0": {"{": "t1", "}": "t2"},
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i, line_num)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t1":
                return TransitionState.COMPLETE, "lbrace", self.value
            if self.state == "t2":
                return TransitionState.COMPLETE, "rbrace", self.value
            else:
                return TransitionState.FAIL, None, None
