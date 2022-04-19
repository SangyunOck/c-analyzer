# 메모리 위에 올라가지 못하는 경우를 방지하기 위해 buffer 설정
class LineBuffer:
    line_counter = 0
    current_line = ""

    def __init__(self, filename) -> None:
        self.filename = filename

    def read_next(self):    
        try:
            line_idx = 0
            prev_line_len = 0
            index = 0
            with open(self.filename) as f:
                line = f.readline()
                prev_line_len = len(line)
                tokens = list(line)
                while True:
                    if prev_line_len == index:
                        line = f.readline()
                        index = 0
                        if line == '':
                            break
                        prev_line_len = len(line)
                        line_idx += 1
                        tokens = list(line)
                    for char in tokens:
                        index += 1
                        if line == '':
                            break
                        yield (char, line_idx)

        except FileNotFoundError:
            print("File not found")
        except Exception:
            print("UnExpected Error")
