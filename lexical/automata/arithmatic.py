from lexical.dfa import DFA

class Arithmatic(DFA):
    states = {
        "t0" : {"+": "t1"},
        "t0": {"-": "t2"},
        "t0": {"*": "t3"},
        "t0": {"/": "t4"},
    }
