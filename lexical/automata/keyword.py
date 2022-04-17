from lexical.dfa import DFA


class Keyword(DFA):
    states = {
        "t0": {
            "i": "t1",
            "e": "t1",
            "w": "t1",
            "r": "t1",
            "I": "t2",
            "E": "t2",
            "W": "t2",
            "R": "t2",
        },
        "t1": {"f": "t3", "l": "t3", "h": "t3", "e": "t3"},
        "t2": {"F": "t4", "L": "t4", "H": "t4", "E": "t4"},
        "t3": {"s": "t5", "i": "t5", "t": "t5"},
        "t4": {"S": "t6", "I": "t6", "T": "t6"},
        't5': {}
    }
