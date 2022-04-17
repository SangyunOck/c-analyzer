from lexical.dfa import DFA, OPERATOR, PROGRAM_KEYWORD, WHITESPACE, LexicalError


class SignedInteger(DFA):
    states = {
        "t0": {
            "0": "t1",
            "-": "t2",
            "1": "t3",
            "2": "t3",
            "3": "t3",
            "4": "t3",
            "5": "t3",
            "6": "t3",
            "7": "t3",
            "8": "t3",
            "9": "t3",
        },
        "t2": {
            "1": "t3",
            "2": "t3",
            "3": "t3",
            "4": "t3",
            "5": "t3",
            "6": "t3",
            "7": "t3",
            "8": "t3",
            "9": "t3",
        },
        "t3": {
            "0": "t4",
            "1": "t4",
            "2": "t4",
            "3": "t4",
            "4": "t4",
            "5": "t4",
            "6": "t4",
            "7": "t4",
            "8": "t4",
            "9": "t4",
        },
        "t4": {
            "0": "t4",
            "1": "t4",
            "2": "t4",
            "3": "t4",
            "4": "t4",
            "5": "t4",
            "6": "t4",
            "7": "t4",
            "8": "t4",
            "9": "t4",
        },
    }

    def accept(self, i, line_num):
        try:
            self.state = self.states[self.state][i]
            self.value += i
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
            if self.state in ["t3", "t4"]:
                if i in WHITESPACE + OPERATOR + PROGRAM_KEYWORD:
                    returnVal = self.value
                    self.reset()
                    return True, int(returnVal)
                else:
                    raise LexicalError(
                        "Only numerical value available after number", line_num
                    )

        return False, None
