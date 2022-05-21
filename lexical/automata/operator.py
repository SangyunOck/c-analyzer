from lexical.dfa import DFA, TransitionState


class Operator(DFA):
    states = {
        "t0": {"<": "t1", ">": "t2", "=": "t3", "!": "t4"},
        "t1": {"=": "t5"},
        "t2": {"=": "t6"},
        "t3": {"=": "t7"},
        "t4": {"=": "t8"},
    }

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i, line_num)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state == "t1":
                return TransitionState.COMPLETE, "comp", self.value
            if self.state == "t2":
                return TransitionState.COMPLETE, "comp", self.value
            if self.state == "t3":
                return TransitionState.COMPLETE, "assign", self.value
            if self.state == "t4":
                return TransitionState.FAIL, None, None
            if self.state == "t5":
                return TransitionState.COMPLETE, "comp", self.value
            if self.state == "t6":
                return TransitionState.COMPLETE, "comp", self.value
            if self.state == "t7":
                return TransitionState.COMPLETE, "comp", self.value
            if self.state == "t8":
                return TransitionState.COMPLETE, "comp", self.value
            else:
                return TransitionState.FAIL, None, None
