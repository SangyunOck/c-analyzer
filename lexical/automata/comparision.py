from lexical.dfa import DFA


class SameComparision(DFA):
    states = {"t0": {"=": "t1"}, "t1": {"=": "t2"}}

    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, None, None
        except KeyError:
            if self.state == "t2":
                returnVal = self.value
                self.reset()
                return True, "SAMECOMPARISION", returnVal
            else:
                self.reset()
                return False, None, None


class NotSameComparision(DFA):
    states = {"t0": {"!": "t1"}, "t1": {"=": "t2"}}

    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, None, None

        except KeyError:
            if self.state == "t2":
                returnVal = self.value
                self.reset()
                return True, "NOTSAMECOMPARISION", returnVal
            else:
                self.reset()
                return False, None, None


class SmallOrSameComparision(DFA):
    states = {"t0": {"<": "t1"}, "t1": {"=":"t2"}}

    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, None, None
        except KeyError:
            if self.state == "t2":
                returnVal = self.value
                self.reset()
                return True, "SMALLORSAMECOMPARISION", returnVal
            else:
                self.reset()
                return False, None, None


class BiggerOrSameComparision(DFA):
    states = {"t0": {">": "t1"}, "t1": {"=": "t2"}}

    def accept(self, i) -> None:
        try:
            super().accept(i)
            return True, None, None
        except KeyError:
            if self.state == "t2":
                returnVal = self.value
                self.reset()
                return True, "BIGGERORSAMECOMPARISION", returnVal
            else:
                return False, None, None


class BiggerComparision(DFA):
    states = {"t0": {">": "t1"}}
    
    def accept(self, i) -> None:
        try:
            super().accept(i)
            returnVal = self.value
            self.reset()
            return True, "BIGGERCOMPARISION", returnVal
        except KeyError:
            return False, None, None


class SmallerComparision(DFA):
    states = {"t0": {"<": "t1"}}
    
    def accept(self, i) -> None:
        try:
            super().accept(i)
            returnVal = self.value
            self.reset()
            return True, "SMALLERCOMPARISION", returnVal
        except KeyError:
            return False, None, None


class Comparision(DFA):
    def __init__(self) -> None:
        self.bigger_comparision = BiggerComparision()
        self.smaller_comparision = SmallerComparision()
        self.same_comparision = SameComparision()
        self.not_same_comparision = NotSameComparision()
        self.smmaller_or_same_pomparision = SmallOrSameComparision()
        self.bigger_or_same_pomparision = BiggerOrSameComparision()

    def accept(self, i, line_num) -> None:
        (
            is_same_comparision_accepted,
            same_comparision_type,
            same_comparision_value,
        ) = self.same_comparision.accept(i)
        if is_same_comparision_accepted and same_comparision_value:
            return is_same_comparision_accepted, same_comparision_type, same_comparision_value
        (
            is_not_same_comparision_accepted,
            not_same_comparision_type,
            not_same_comparision_value,
        ) = self.not_same_comparision.accept(i)
        if is_not_same_comparision_accepted and not_same_comparision_value:
            return is_not_same_comparision_accepted, not_same_comparision_type, not_same_comparision_value
        (
            is_smmaller_or_same_pomparision_accepted,
            smmaller_or_same_pomparision_type,
            smmaller_or_same_pomparision_value,
        ) = self.smmaller_or_same_pomparision.accept(i)
        if is_smmaller_or_same_pomparision_accepted and smmaller_or_same_pomparision_value:
            return is_smmaller_or_same_pomparision_accepted, smmaller_or_same_pomparision_type, smmaller_or_same_pomparision_value
        (
            is_bigger_or_same_pomparision_accepted,
            bigger_or_same_pomparision_type,
            bigger_or_same_pomparision_value,
        ) = self.bigger_or_same_pomparision.accept(i)
        if is_bigger_or_same_pomparision_accepted and bigger_or_same_pomparision_value:
            return is_bigger_or_same_pomparision_accepted, bigger_or_same_pomparision_type, bigger_or_same_pomparision_value
        (
            is_bigger_comparision_accepted,
            bigger_comparision_type,
            bigger_comparision_value,
        ) = self.bigger_comparision.accept(i)
        if is_bigger_comparision_accepted and bigger_comparision_value:
            return is_bigger_comparision_accepted, bigger_comparision_type, bigger_comparision_value

        (
            is_smaller_comparision_accepted,
            smaller_comparision_type,
            smaller_comparision_value,
        ) = self.smaller_comparision.accept(i)
        if is_smaller_comparision_accepted and smaller_comparision_value:
            return is_smaller_comparision_accepted, smaller_comparision_type, smaller_comparision_value
