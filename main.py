import sys  
from lexical.lexical_analyzer import LexicalAnalyzer

if __name__ == "__main__":
    filename = sys.argv[1]
    lexical_analyzer = LexicalAnalyzer(filename)
    lexical_analyzer.scan_lexemes()
