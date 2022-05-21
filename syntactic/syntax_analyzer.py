from syntactic.symbol_manager import get_rules, get_slr_grammar
from syntactic.stack import Stack
from syntactic.models import SLRGrammarData
from typing import Dict


class SyntaxAnalyzer:

    rules = {}
    stack = Stack()
    input_string = []
    slr_grammar: Dict[int, SLRGrammarData]
    output_file = None

    def __init__(self, input_string):
        self.rules = get_rules()
        self.stack.push(0)
        self.input_string = input_string
        self.slr_grammar = get_slr_grammar()
        self.output_file = open("test.out", "a")

    def parse_sytax(self):
        splitter_index = 0
        
        while True:
            current_state = self.stack.peek()
            current_input_string, current_input_value, line_num = self.input_string[splitter_index]
            command: str = self.rules[current_state][current_input_string]

            if command.startswith("s"):
                splitter_index += 1
                self.stack.push(int(command.strip("s")))

            if command.startswith("r"):
                reduce_num = int(command.strip("r"))

                lhs = self.slr_grammar[reduce_num].lhs
                rhs_len = int(self.slr_grammar[reduce_num].rhs_length)
                
                self.stack.pop(rhs_len)
                current_state = self.stack.peek()
                new_state = int(self.rules[current_state][lhs])
                self.stack.push(new_state)

            if command.startswith("acc"):
                self.output_file.write("\n\n")
                self.output_file.write("accepted!")
                break

            if command == ' ':
                self.output_file.write("\n\n")
                self.output_file.write(f'error at "{current_input_value}", line {line_num}')
                break

        self.output_file.close()
