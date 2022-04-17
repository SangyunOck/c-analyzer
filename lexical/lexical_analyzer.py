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
                    lexeme = grammar.check_lexeme(token, line_num)
                    if lexeme:
                        print(lexeme)
                except LexicalError as e:
                    print(e)
                    self.output_file.write(e.msg)
                    break

        self.output_file.close()
