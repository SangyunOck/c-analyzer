# 메모리 위에 올라가지 못하는 경우를 방지하기 위해 buffer 설정
class LineBuffer:
    line_counter = 0
    current_line = ""

    def __init__(self, filename) -> None:
        self.filename = filename

    def read_next(self):
        try:
            with open(self.filename) as f:
                while True:
                    self.current_line = f.readline()
                    if self.current_line == "" or self.current_line is None:
                        break

                    self.line_counter += 1
                    self.tokens = list(self.current_line)
                    for token in self.tokens:
                        yield (token, self.line_counter)

        except FileNotFoundError:
            print("File not found")
        except Exception:
            print("UnExpected Error")
