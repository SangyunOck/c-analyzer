from lexical.dfa import WHITESPACE, LexicalError
from lexical.grammar import Grammar
from tools.line_buffer import LineBuffer


class LexicalAnalyzer:
    def __init__(self, filename):
        self.line_buffer = LineBuffer(filename)
        self.output_file = open("test.out", "a")

    def _write_to_file(self, accepted, token_type, token_value):
        if accepted and token_type != "WHITESPACE" and token_value:
            print(token_type, token_value)

    def scan_lexemes(self):
        grammar = Grammar()
        token, line_num = self.line_buffer.pop()
    
        while True:
            try:
                if token:
                    accepted, token_type, token_value = grammar.check_lexeme(token, line_num)
                    if accepted:
                        token, line_num = self.line_buffer.pop()
                        self._write_to_file(accepted, token_type, token_value)
            except IndexError:
                self._write_to_file(accepted, token_type, token_value)
                accepted, token_type, token_value = grammar.check_lexeme(token, line_num)
                self._write_to_file(accepted, token_type, token_value)
                break
            except LexicalError as e:
                self.output_file.write(e.msg)
                break

        self.output_file.close()
