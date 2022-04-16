from tools.line_buffer import LineBuffer

class LexicalAnalyzer:
    line = ""
    def __init__(self, filename):
        self.line_buffer = LineBuffer(filename)
