import re
from lexical.dfa import DFA


class IFKeyword(DFA):
    states = {
        "t0": {"i": "t1", "I": "t2"},
        "t1": {"f": "t3"},
        "t2": {"F": "t4"}
    }
    def accept(self, i) -> None:
        try:
            super().accept(i)
        except KeyError:
            if self.state in ["t3", "t4"]:
                return True, self.value
            else:
                return False, None

class ElSEKeyword(DFA):
    states = {
        "t0": {"e": "t1"},
        "t0": {"E": "t2"},
        "t1": {"l": "t3"},
        "t2": {"L": "t4"},
        "t3": {"s": "t5"},
        "t4": {"S": "t6"},
        "t5": {"e": "t7"},
        "t6": {"E": "t8"}
    }
    def accept(self, i) -> None:
        try:
            super().accept(i)
        except KeyError:
            if self.state in ["t7", "t8"]:
                return True, self.value
            else:
                return False, None


class WHILEKeyword(DFA):
    states = {
        "t0": {"w": "t1"},
        "t0": {"W": "t2"},
        "t1": {"h": "t3"},
        "t2": {"H": "t4"},
        "t3": {"i": "t5"},
        "t4": {"I": "t6"},
        "t5": {"l": "t7"},
        "t6": {"L": "t8"},
        "t7": {"e": "t9"},
        "t8": {"E": "t10"}
    }
    def accept(self, i) -> None:
        try:
            super().accept(i)
        except KeyError:
            if self.state in ["t9", "t10"]:
                return True, self.value
            else:
                return False, None


class RETURNKeyword(DFA):
    states = {
        "t0": {"r": "t1"},
        "t0": {"R": "t2"},
        "t1": {"e": "t3"},
        "t2": {"E": "t4"},
        "t3": {"t": "t5"},
        "t4": {"T": "t6"},
        "t5": {"u": "t7"},
        "t6": {"U": "t8"},
        "t7": {"r": "t9"},
        "t8": {"R": "t10"},
        "t9": {"n": "t11"},
        "t10": {"N": "t12"}
    }
    def accept(self, i) -> None:
        try:
            super().accept(i)
        except KeyError:
            if self.state in ["t9", "t10"]:
                return True, self.value
            else:
                return False, None


    

