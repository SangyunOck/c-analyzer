from prettytable import PrettyTable

from lexical.dfa import NON_ZERO_DIGIT, SPECIAL_CHARS, LexicalError, TransitionState
from lexical.grammar import Grammar
from tools.line_buffer import LineBuffer


class LexicalAnalyzer:
    def __init__(self, filename):
        self.tokens = []
        self.line_buffer = LineBuffer(filename)
        self.output_file = open("test.out", "w")
        self.table = PrettyTable(["Token name", "Token value"])
        self.minus_counter = 0
        self.prev_token_type = ""

    # 테이블에 토큰을 추가하는 메소드
    def _add_to_table(self, accepted, token_type, token_value, line_num):
        if (
            accepted != TransitionState.FAIL
            and token_type != "WHITESPACE"
            and token_value
        ):
            self.table.add_row([token_type, token_value])
            self.tokens.append((token_type, token_value, line_num))

    # 한글짜씩 읽어 오토마타의 transition을 일으키는 메소드
    def scan_lexemes(self):
        grammar = Grammar()
        token = ""

        try:
            token, line_num = self.line_buffer.pop()
        except Exception:
            return

        while True:
            try:
                if token:
                    if token in SPECIAL_CHARS:
                        self.output_file.write(
                            "Special characters not allowed, " + str(line_num) + "\n"
                        )
                        break
                    accepted, token_type, token_value = grammar.check_lexeme(
                        token, line_num
                    )
                    # transition에 실패 후, 오토마타의 state가 final state일 때 complete을 반환
                    # -, 0과 관련된 후처리를 하기 위한 구문
                    if accepted == TransitionState.COMPLETE:
                        if (token_type, token_value) == ("num", "0"):
                            for _ in range(self.minus_counter):
                                self._add_to_table(accepted, "addsub", "-", line_num)
                                self.minus_counter -= 1

                        if token_value in NON_ZERO_DIGIT:
                            if self.prev_token_type in ["id", "num"]:
                                if self.minus_counter == 1:
                                    self._add_to_table(accepted, "addsub", "-", line_num)
                                    self.minus_counter = 0

                                elif self.minus_counter == 2:
                                    self._add_to_table(accepted, "addsub", "-", line_num)
                                    token_value = "-" + token_value
                                    self.minus_counter = 0
                            else:
                                if self.minus_counter == 1:
                                    self.minus_counter -= 1
                                    token_value = "-" + token_value
                                elif self.minus_counter == 2:
                                    self._add_to_table(accepted, "addsub", "-", line_num)
                                    token_value = "-" + token_value
                                    self.minus_counter = 0

                        if token_value != "-":
                            for _ in range(self.minus_counter):
                                self._add_to_table(accepted, "addsub", "-", line_num)
                                self.minus_counter -= 1
                            self._add_to_table(accepted, token_type, token_value, line_num)
                            self.prev_token_type = token_type

                        elif token_value == "-":
                            if self.minus_counter == 2:
                                self._add_to_table(accepted, "addsub", "-", line_num)
                            else:
                                self.minus_counter += 1
                        # 성공적으로 토큰을 반환하면 모든 오토마타의 state를 초기화
                        grammar.reset_all_states()
                        # 오토마타의 transition이 성공하면 새로운 문자를 가져옴
                    elif accepted in [TransitionState.SUCCESS, TransitionState.FAIL]:
                        token, line_num = self.line_buffer.pop()
            # 마지막 문자까지 가져온 후 현재 체크중인 문자로 한번 더 확인
            except IndexError:
                accepted, token_type, token_value = grammar.check_lexeme(
                    token, line_num
                )
                self._add_to_table(accepted, token_type, token_value, line_num)
                if not grammar.is_accepted():
                    self.output_file.write(
                        'Need " to complete string, ' + str(line_num) + "\n"
                    )
                break
            except LexicalError as e:
                self.output_file.write(e.msg + "\n")
                break

        self.output_file.write(str(self.table))
        self.output_file.close()
        self.tokens.append(("$", "ENDMARKER", line_num))
        
        return self.tokens
