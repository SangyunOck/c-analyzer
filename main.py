from lexical.lexical_analyzer import LexicalAnalyzer


if __name__ == "__main__":
    print("Input file name: ")
    filename = input().strip()
    lexical_analyzer = LexicalAnalyzer(filename)
    