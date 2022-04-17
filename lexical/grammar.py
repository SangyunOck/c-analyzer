from lexical.automata.signed_int import SignedInteger
from lexical.automata.variable import VariableType


class Grammar:
    def __init__(self) -> None:
        self.variable_type = VariableType()
        self.signed_integer = SignedInteger()

    def check_lexeme(self, i, line_num):
        is_variable_type_accepted, variable_type_value = self.variable_type.accept(
            i, line_num
        )
        is_signed_integer_accepted, signed_integer_value = self.signed_integer.accept(
            i, line_num
        )

        print(is_variable_type_accepted, variable_type_value)
        print(is_signed_integer_accepted, signed_integer_value)
