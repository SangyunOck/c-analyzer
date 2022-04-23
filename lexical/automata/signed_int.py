from lexical.dfa import DFA, LexicalError, TransitionState, WHITESPACE, PROGRAM_KEYWORD, ARITHMATIC_OPERATOR

non_zero_digits = [str(i) for i in range(1, 10)]
digits = non_zero_digits + [0]


class SignedInteger(DFA):
    states = {}
    states["t0"] = {i: "t3" for i in non_zero_digits}
    states["t0"]["0"] = "t1"
    states["t0"]["-"] = "t2"

    states["t2"] = {i: "t3" for i in non_zero_digits}
    states["t3"] = {i: "t3" for i in digits}

    def accept(self, i, line_num) -> None:
        try:
            super().accept(i)
            return TransitionState.SUCCESS, None, None
        except KeyError:
            if self.state in ["t1", "t3", "t4"]:
                if i in WHITESPACE + PROGRAM_KEYWORD + ARITHMATIC_OPERATOR:
                    return TransitionState.COMPLETE, "SIGNEDINTEGER", self.value
                else:
                    raise LexicalError("Variable cannot start with numerical value", line_num)
            if self.state == "t2":
                raise LexicalError("Numerical value needed after '-'", line_num)
            else:
                return TransitionState.FAIL, None, None

