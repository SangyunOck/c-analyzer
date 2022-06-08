from syntactic.models import SLRGrammarData

symbols = [
    "vtype",
    "id",
    "semi",
    "lparen",
    "rparen",
    "lbrace",
    "rbrace",
    "comma",
    "assign",
    "if",
    "else",
    "while",
    "literal",
    "addsub",
    "multdiv",
    "num",
    "comp",
    "return",
    "$",
    "CODEPRIME",
    "CODE",
    "VDECL",
    "FDECL",
    "ARG",
    "MOREARGS",
    "BLOCK",
    "STMT",
    "RHS",
    "EXPR",
    "TERM",
    "FACTOR",
    "COND",
    "RETURN",
]

states = {
    "0": [
        "s4",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r3",
        " ",
        "1",
        "2",
        "3",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "1": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "acc",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "2": [
        "s4",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r3",
        " ",
        "5",
        "2",
        "3",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "3": [
        "s4",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r3",
        " ",
        "6",
        "2",
        "3",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "4": [
        " ",
        "s7",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "5": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r1",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "6": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r2",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "7": [
        " ",
        " ",
        "s8",
        "s9",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "8": [
        "r4",
        "r4",
        " ",
        " ",
        " ",
        " ",
        "r4",
        " ",
        " ",
        "r4",
        " ",
        "r4",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r4",
        "r4",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "9": [
        "s11",
        " ",
        " ",
        " ",
        "r7",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "10",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "10": [
        " ",
        " ",
        " ",
        " ",
        "s12",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "11": [
        " ",
        "s13",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "12": [
        " ",
        " ",
        " ",
        " ",
        " ",
        "s14",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "13": [
        " ",
        " ",
        " ",
        " ",
        "r9",
        " ",
        " ",
        "s16",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "15",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "14": [
        "s23",
        "s20",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        "s21",
        " ",
        "s22",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        " ",
        "19",
        " ",
        " ",
        " ",
        "17",
        "18",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "15": [
        " ",
        " ",
        " ",
        " ",
        "r6",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "16": [
        "s24",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "17": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s26",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "25",
    ],
    "18": [
        "s23",
        "s20",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        "s21",
        " ",
        "s22",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        " ",
        "19",
        " ",
        " ",
        " ",
        "27",
        "18",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "19": [
        "r12",
        "r12",
        " ",
        " ",
        " ",
        " ",
        "r12",
        " ",
        " ",
        "r12",
        " ",
        "r12",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r12",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "20": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s28",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "21": [
        " ",
        " ",
        " ",
        "s29",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "22": [
        " ",
        " ",
        " ",
        "s30",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "23": [
        " ",
        "s31",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "24": [
        " ",
        "s32",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "25": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s33",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "26": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "34",
        " ",
        " ",
    ],
    "27": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r10",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r10",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "28": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s40",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "38",
        "39",
        "41",
        "42",
        " ",
        " ",
    ],
    "29": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "44",
        "43",
        " ",
    ],
    "30": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "44",
        "45",
        " ",
    ],
    "31": [
        " ",
        " ",
        "s8",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "32": [
        " ",
        " ",
        " ",
        " ",
        "r9",
        " ",
        " ",
        "s16",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "46",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "33": [
        "r5",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r5",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "34": [
        " ",
        " ",
        "s47",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "35": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "48",
        "41",
        "42",
        " ",
        " ",
    ],
    "36": [
        " ",
        " ",
        "r23",
        " ",
        "r23",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r23",
        "r23",
        " ",
        "r23",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "37": [
        " ",
        " ",
        "r24",
        " ",
        "r24",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r24",
        "r24",
        " ",
        "r24",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "38": [
        " ",
        " ",
        "s49",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "39": [
        " ",
        " ",
        "r16",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "40": [
        " ",
        " ",
        "r17",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "41": [
        " ",
        " ",
        "r19",
        " ",
        "r19",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s50",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "42": [
        " ",
        " ",
        "r21",
        " ",
        "r21",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r21",
        "s51",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "43": [
        " ",
        " ",
        " ",
        " ",
        "s52",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "44": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s53",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "45": [
        " ",
        " ",
        " ",
        " ",
        "s54",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "46": [
        " ",
        " ",
        " ",
        " ",
        "r8",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "47": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r26",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "48": [
        " ",
        " ",
        " ",
        " ",
        "s55",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "49": [
        "r13",
        "r13",
        " ",
        " ",
        " ",
        " ",
        "r13",
        " ",
        " ",
        "r13",
        " ",
        "r13",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r13",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "50": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "56",
        "41",
        "42",
        " ",
        " ",
    ],
    "51": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "57",
        "42",
        " ",
        " ",
    ],
    "52": [
        " ",
        " ",
        " ",
        " ",
        " ",
        "s58",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "53": [
        " ",
        "s36",
        " ",
        "s35",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s37",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "59",
        " ",
        " ",
    ],
    "54": [
        " ",
        " ",
        " ",
        " ",
        " ",
        "s60",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "55": [
        " ",
        " ",
        "r22",
        " ",
        "r22",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r22",
        "r22",
        " ",
        "r22",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "56": [
        " ",
        " ",
        "r18",
        " ",
        "r18",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "57": [
        " ",
        " ",
        "r20",
        " ",
        "r20",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r20",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "58": [
        "s23",
        "s20",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        "s21",
        " ",
        "s22",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        " ",
        "19",
        " ",
        " ",
        " ",
        "61",
        "18",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "59": [
        " ",
        " ",
        " ",
        " ",
        "r25",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "60": [
        "s23",
        "s20",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        "s21",
        " ",
        "s22",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        " ",
        "19",
        " ",
        " ",
        " ",
        "62",
        "18",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "61": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s63",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "62": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s64",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "63": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s65",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "64": [
        "r15",
        "r15",
        " ",
        " ",
        " ",
        " ",
        "r15",
        " ",
        " ",
        "r15",
        " ",
        "r15",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r15",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "65": [
        " ",
        " ",
        " ",
        " ",
        " ",
        "s66",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "66": [
        "s23",
        "s20",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        "s21",
        " ",
        "s22",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r11",
        " ",
        " ",
        " ",
        "19",
        " ",
        " ",
        " ",
        "67",
        "18",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "67": [
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        "s68",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
    "68": [
        "r14",
        "r14",
        " ",
        " ",
        " ",
        " ",
        "r14",
        " ",
        " ",
        "r14",
        " ",
        "r14",
        " ",
        " ",
        " ",
        " ",
        " ",
        "r14",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
        " ",
    ],
}

CFG = \
'''
CODEPRIME > CODE
CODE > VDECL CODE
CODE > FDECL CODE
CODE > ''
VDECL > vtype id semi
FDECL > vtype id lparen ARG rparen lbrace BLOCK RETURN rbrace
ARG > vtype id MOREARGS
ARG > ''
MOREARGS > comma vtype id MOREARGS
MOREARGS > ''
BLOCK > STMT BLOCK
BLOCK > ''
STMT > VDECL
STMT > id assign RHS semi
STMT > if lparen COND rparen lbrace BLOCK rbrace else lbrace BLOCK rbrace
STMT > while lparen COND rparen lbrace BLOCK rbrace
RHS > EXPR
RHS > literal
EXPR > TERM addsub EXPR
EXPR > TERM
TERM > FACTOR multdiv TERM
TERM > FACTOR
FACTOR > lparen EXPR rparen
FACTOR > id
FACTOR > num
COND > FACTOR comp FACTOR
RETURN > return FACTOR semi
'''

# 정의된 규칙을 dict형태로 반환
def get_rules():
    rules = {}
    
    for state, transition in states.items():
        for idx, t in enumerate(transition):
            state = int(state)
            if state in rules.keys():
                rules[state][symbols[idx]] = t
            else:
                rules[state] = {symbols[idx]: t}

    return rules

# CFG를 파싱하여 reduce가 어떻게 진행되는지 반환
def get_slr_grammar():
    slr_grammer = {}

    for idx, item in enumerate(CFG.strip().split("\n")):
        lhs, rhs = item.split(">")
        splited_rhs = rhs.strip().split()
        rhs_len = len(splited_rhs)
        if splited_rhs == ["''"]:
            rhs_len = 0

        slr_grammer[idx] = SLRGrammarData(lhs=lhs.strip(), rhs_length=rhs_len)
        
    return slr_grammer
