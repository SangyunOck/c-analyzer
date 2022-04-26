from lexical.dfa import DFA, TransitionState


class WhiteSpace(DFA):
    states = {
        "t0": {"\n": "t1", "\0": "t2", "\t": "t3", " ": "t4"},
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i, line_num)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t1", "t2", "t3", "t4"]:
                return TransitionState.COMPLETE, "WHITESPACE", self.value
            else:
                return TransitionState.FAIL, None, None
