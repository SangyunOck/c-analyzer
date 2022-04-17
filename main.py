from lexical.lexical_analyzer import LexicalAnalyzer

if __name__ == "__main__":
    print("Input file name: ", end="")
    filename = input().strip()
    lexical_analyzer = LexicalAnalyzer(filename)
    lexical_analyzer.scan_lexemes()
