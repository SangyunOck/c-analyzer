from tools.line_buffer import LineBuffer
from .grammar import Grammar, GrammarError

class LexicalAnalyzer:
    def __init__(self, filename):
        self.line_buffer = LineBuffer(filename)
        self.output_file = open("test.out", "a")

    def scan_lexemes(self):
        grammar = Grammar()
        buffer = []

        for line_idx, line in self.line_buffer.read_next():
            tokens = list(line)
            try:
                for i in tokens:
                    buffer.append(i)
                    print(buffer)
                    parse_result = grammar.get_lexeme(line_idx, buffer)

                    if parse_result and parse_result != "WHITESPACE":
                        print(parse_result)
                        self.output_file.write(parse_result + " ")
                        buffer.clear()
        
                    if parse_result == "WHITESPACE":
                        buffer.clear()
        
                self.output_file.write("\n")

            except GrammarError as e:
                    print(e)
                    self.output_file.write(e.msg)
                    break
        self.output_file.close()

    
