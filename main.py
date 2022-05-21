import sys

from lexical.lexical_analyzer import LexicalAnalyzer
from syntactic.syntax_analyzer import SyntaxAnalyzer

if __name__ == "__main__":
    filename = "test.c"
    lexical_analyzer = LexicalAnalyzer(filename)
    input_string = lexical_analyzer.scan_lexemes()
    syntax_analyzer = SyntaxAnalyzer(input_string)
    syntax_analyzer.parse_sytax()