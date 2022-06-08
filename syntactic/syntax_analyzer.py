from syntactic.symbol_manager import get_rules, get_slr_grammar
from syntactic.stack import Stack
from syntactic.models import SLRGrammarData
from typing import Dict


class SyntaxAnalyzer:

    rules = {}
    stack = Stack()
    input_string = []
    slr_grammar: Dict[int, SLRGrammarData]
    output_file = None

    # lexical analyzer가 분석한 라인과, 정의된 규칙을 가져옴
    def __init__(self, input_string):
        self.rules = get_rules()
        self.stack.push(0)
        self.input_string = input_string
        self.slr_grammar = get_slr_grammar()
        self.output_file = open("test.out", "a")

    def parse_sytax(self):
        splitter_index = 0
        
        while True:
            current_state = self.stack.peek()
            current_input_string, current_input_value, line_num = self.input_string[splitter_index]
            # 현재 state에서 인풋 스트링에 따라 룰에 기반한 행동을 결정함
            command: str = self.rules[current_state][current_input_string]

            # 커맨드가 shift이면 splitter의 인덱스를 하나 증가시키고 stack에 shift한 상태를 push함
            if command.startswith("s"):
                splitter_index += 1
                self.stack.push(int(command.strip("s")))

            # 커맨드가 reduce이면
            if command.startswith("r"):
                reduce_num = int(command.strip("r"))
                # r뒤에 오는 숫자를 확인하여 reduce 후 state를 결정
                lhs = self.slr_grammar[reduce_num].lhs
                rhs_len = int(self.slr_grammar[reduce_num].rhs_length)
                # reduce된 길이만큼 스택에서 pop
                self.stack.pop(rhs_len)
                # pop 된 이후 stack의 가장 위의 state로 업데이트하여 다시 push
                current_state = self.stack.peek()
                new_state = int(self.rules[current_state][lhs])
                self.stack.push(new_state)

            # 커맨드가 accept됐다면 결과로 출력
            if command.startswith("acc"):
                self.output_file.write("\n\n")
                self.output_file.write("accepted!")
                break
            
            # 에러 핸들링
            if command == ' ':
                self.output_file.write("\n\n")
                self.output_file.write(f'error at "{current_input_value}", line {line_num}')
                break

        self.output_file.close()
