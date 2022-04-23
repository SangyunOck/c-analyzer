from lexical.dfa import DFA, TransitionState


class Semicolon(DFA):
    states = {"t0": {";": "t1"}}

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t1":
                return TransitionState.COMPLETE, "SEMICOLON", self.value
            else:
                return TransitionState.FAIL, None, None
