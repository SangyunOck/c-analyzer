
# 파일을 line-by-line으로 읽은 후 한 글자씩 뗴어서 반환하기 위한 클래스
class LineBuffer:
    buffer = []

    def __init__(self, filename):
        try:
            with open(filename) as f:
                total_content = f.readlines()
                lines_len = len(total_content)
                self.buffer.append((" ", lines_len))
                # 스택 구조를 사용하므로 거꾸로 집어넣음
                for line_num, lexemes in enumerate(reversed(total_content)):
                    for lexeme in reversed(list(lexemes)):
                        self.buffer.append((lexeme, lines_len - line_num))
        except FileNotFoundError:
            print("File not found")

    def pop(self):
        top = self.buffer.pop()
        return top

    def peek(self):
        return self.buffer[-1]
