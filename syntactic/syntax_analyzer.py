from syntactic.slr_table import get_rules
from syntactic.stack import Stack

class SyntaxAnalyzer:
    rules = {}
    stack = Stack()
    def __init__(self) -> None:
        self.rules = get_rules()
        self.stack.push(0)
        print(self.rules)
