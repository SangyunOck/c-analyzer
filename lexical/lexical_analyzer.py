from lexical.dfa import WHITESPACE, LexicalError
from lexical.grammar import Grammar
from tools.line_buffer import LineBuffer


class LexicalAnalyzer:
    def __init__(self, filename):
        self.line_buffer = LineBuffer(filename)
        self.output_file = open("test.out", "a")

    def scan_lexemes(self):
        grammar = Grammar()

        for token, line_num in self.line_buffer.read_next():
            if token not in WHITESPACE:
                try:
                    token_type, token_value = grammar.check_lexeme(token, line_num)
                    if token_type:
                        print(token_type, token_value)
                except LexicalError as e:
                    print(e)
                    self.output_file.write(e.msg)
                    break

        self.output_file.close()
