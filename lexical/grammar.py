from automata.arithmatic import Arithmatic
from automata.assignment import Assignment
from automata.comma import Comma
from automata.comparision import Comparision
from automata.identifier import Identifier
from automata.keyword import Keyword
from automata.literal_string import LiteralString
from automata.semicolon import Semicolon
from automata.signed_int import SignedInteger
from automata.symbols_for_defining import SymbolsForDefining
from automata.symbols_for_indicating import SymbolsForIndicating
from automata.variable import VariableType


class Grammar:
    def __init__(self) -> None:
        self.arithmatic = Arithmatic()
        self.assignment = Assignment()
        self.comma = Comma()
        self.comparison = Comparision()
        self.identifier = Identifier()
        self.keyword = Keyword()
        self.literal_string = LiteralString()
        self.semicolon = Semicolon()
        self.signed_integer = SignedInteger()
        self.symbols_for_defining = SymbolsForDefining()
        self.symbols_for_indicating = SymbolsForIndicating()
        self.variable_type = VariableType()

    def check_lexeme(self, i, line_num):
        is_arithmatic_accepted, arithmatic_type, arithmatic_value = self.arithmatic.accept(i, line_num)
        if is_arithmatic_accepted and arithmatic_value:
            return arithmatic_type, arithmatic_value

        is_assignment_accepted, assignment_type, assignment_value  = self.assignment.accept(i, line_num)
        if is_assignment_accepted and assignment_value:
            return assignment_type, assignment_value

        is_comma_accepted, comma_type, comma_value  = self.comma.accept(i, line_num)
        if is_comma_accepted and comma_value:
            return comma_type, comma_value

        is_comparison_accepted, comparison_type, comparison_value = self.comparison.accept(i, line_num)
        if is_comparison_accepted and comparison_value:
            return comparison_type, comparison_value


        is_identifier_accepted, identifier_type, identifier_value = self.identifier.accept(i, line_num)
        if is_identifier_accepted and identifier_value:
            return identifier_type, identifier_value

        is_keyword_accepted, keyword_type, keyword_value = self.keyword.accept(i, line_num)
        if is_keyword_accepted and keyword_value:
            return keyword_type, keyword_value

        is_literal_string_accepted, literal_string_type, literal_string_value = self.literal_string.accept(
            i, line_num
        )
        if is_literal_string_accepted and literal_string_value:
            return literal_string_type, literal_string_value
        
        is_semicolon_accepted, semicolon_type, semicolon_value = self.semicolon.accept(i, line_num)
        if is_semicolon_accepted and semicolon_value:
            return semicolon_type, semicolon_value

        is_signed_integer_accepted, signed_integer_type, signed_integer_value = self.signed_integer.accept(
            i, line_num
        )
        if is_signed_integer_accepted and signed_integer_value:
            return signed_integer_type, signed_integer_value

        (
            is_symbols_for_defining_accepted,
            symbols_for_defining_type,
            symbols_for_defining_value,
        ) = self.symbols_for_defining.accept(i, line_num)
        if is_symbols_for_defining_accepted and symbols_for_defining_value:
            return symbols_for_defining_type, symbols_for_defining_value

        (
            is_symbols_for_indicating_accepted,
            symbols_for_indicating_type,
            symbols_for_indicating_value,
        ) = self.symbols_for_indicating.accept(i, line_num)
        if is_symbols_for_indicating_accepted and symbols_for_indicating_value:
            return symbols_for_indicating_type, symbols_for_indicating_value

        is_variable_type_accepted, variable_type_type, variable_type_value = self.variable_type.accept(
            i, line_num
        )
        if is_variable_type_accepted and variable_type_value:
            return variable_type_type, variable_type_value
