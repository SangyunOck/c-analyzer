from lexical.dfa import DFA, OPERATOR, PROGRAM_KEYWORD, WHITESPACE, LexicalError

non_zero_digits = [str(i) for i in range(1, 10)]
digits = non_zero_digits + [0]

class SignedInteger(DFA):
    states = {}
    states['t0'] = {i: "t3" for i in non_zero_digits}
    states['t0']['0'] = "t1"
    states['t0']['-'] = "t2"

    states['t2'] = {i: "t3" for i in non_zero_digits}
    states['t3'] = {i: "t3" for i in digits}
    
    def accept(self, i, line_num):
        try:
            super().accept(i)
            if self.state != "t4":
                return True, None
        except KeyError:
            if self.state == "t0":
                return False, None
            if self.state == "t1":
                raise LexicalError(
                    "Variable cannot start with numerical value", line_num
                )
            if self.state == "t2":
                raise LexicalError("Only numerical value available after " - "")
            if self.state == "t3":
                if i in WHITESPACE + OPERATOR + PROGRAM_KEYWORD:
                    returnVal = self.value
                    self.reset()
                    return True, int(returnVal)
                else:
                    raise LexicalError(
                        "Only numerical value available after number", line_num
                    )

        return False, None
