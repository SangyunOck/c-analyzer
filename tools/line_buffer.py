class LineBuffer:
    line_counter = 0
    current_line = ""

    def __init__(self, filename) -> None:
        try:
            with open(filename) as f:
                total_content = f.readlines()
                lines_len = len(total_content)
                self.buffer = [(" ", -1)]
                for line_num, lexemes in enumerate(reversed(total_content)):
                    for lexeme in reversed(list(lexemes)):
                        self.buffer.append((lexeme, lines_len - line_num))
            print(self.buffer)
        except FileNotFoundError:
            print("File not found")

    def pop(self):
        top = self.buffer.pop()
        return top

    def peek(self):
        return self.buffer[-1]