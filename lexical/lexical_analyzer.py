from prettytable import PrettyTable

from lexical.dfa import SPECIAL_CHARS, ALPHABET_LOWER, ALPHABET_UPPER, DIGIT, LexicalError, TransitionState
from lexical.grammar import Grammar
from tools.line_buffer import LineBuffer


class LexicalAnalyzer:
    def __init__(self, filename):
        self.line_buffer = LineBuffer(filename)
        self.output_file = open("test.out", "w")
        self.table = PrettyTable(["Token name", "Token value"])

    def _add_to_table(self, accepted, token_type, token_value):
        if (
            accepted != TransitionState.FAIL
            and token_type != "WHITESPACE"
            and token_value
        ):
            self.table.add_row([token_type, token_value])
            print(token_type, token_value)

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

                    if accepted == TransitionState.COMPLETE:
                        self._add_to_table(accepted, token_type, token_value)
                        grammar.reset_all_states()
                    elif accepted in [TransitionState.SUCCESS, TransitionState.FAIL]:
                        token, line_num = self.line_buffer.pop()

            except IndexError:
                self._add_to_table(accepted, token_type, token_value)
                accepted, token_type, token_value = grammar.check_lexeme(
                    token, line_num
                )
                self._add_to_table(accepted, token_type, token_value)
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
