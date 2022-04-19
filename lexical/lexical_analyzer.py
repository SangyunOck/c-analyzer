from lexical.dfa import WHITESPACE, LexicalError
from lexical.grammar import Grammar
from tools.line_buffer import LineBuffer


class LexicalAnalyzer:
    def __init__(self, filename):
        self.line_buffer = LineBuffer(filename)
        self.output_file = open("test.out", "a")

    def scan_lexemes(self):
        grammar = Grammar()
        is_popped = False
        
        line_buffer = self.line_buffer.read_next()
    
        while True:
            if not is_popped:
                try:
                    token, line_num = next(line_buffer)
                except StopIteration:
                    succeeded, token_type, token_value = grammar.check_lexeme(token, line_num)
                    if token_type and token_value:
                        print(token_type, token_value)
                    break
            if token:
                try:
                    succeeded, token_type, token_value = grammar.check_lexeme(token, line_num)
                    if succeeded:
                        is_popped = False
        
                    if token_type and token_value:
                        print(token_type, token_value)
                        
                    if not succeeded:
                        is_popped = True
                except LexicalError as e:
                    print(e)
                    self.output_file.write(e.msg)
                    break

        self.output_file.close()
