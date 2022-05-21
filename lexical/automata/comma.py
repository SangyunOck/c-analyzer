from lexical.dfa import DFA, TransitionState


class Comma(DFA):
    states = {"t0": {",": "t1"}}

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i, line_num)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t1"]:
                return TransitionState.COMPLETE, "comma", self.value
            else:
                return TransitionState.FAIL, None, None
