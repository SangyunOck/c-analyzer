from lexical.dfa import TransitionState
from lexical.automata.arithmatic import Arithmatic
from lexical.automata.assignment import Assignment
from lexical.automata.comma import Comma
from lexical.automata.comparision import (
    EqualComparision,
    NotEqualComparision,
    SmallerOrEqualComparision,
    BiggerOrEqualComparision,
    BiggerComparision,
    SmallerComparision,
)
from lexical.automata.identifier import Identifier
from lexical.automata.keyword import Keyword
from lexical.automata.literal_string import LiteralString
from lexical.automata.semicolon import Semicolon
from lexical.automata.signed_int import SignedInteger
from lexical.automata.symbols_for_defining import SymbolsForDefining
from lexical.automata.symbols_for_indicating import SymbolsForIndicating
from lexical.automata.variable import VariableType
from lexical.automata.whitespace import WhiteSpace


class Grammar:
    def __init__(self) -> None:
        self.complete_counter = 0
        self.arithmatic = Arithmatic()
        self.assignment = Assignment()
        self.comma = Comma()
        self.equal_comparision = EqualComparision()
        self.not_equal_comparision = NotEqualComparision()
        self.small_or_equal_comparision = SmallerOrEqualComparision()
        self.bigger_or_equal_comparision = BiggerOrEqualComparision()
        self.bigger_comparision = BiggerComparision()
        self.smaller_comparision = SmallerComparision()
        self.identifier = Identifier()
        self.keyword = Keyword()
        self.literal_string = LiteralString()
        self.semicolon = Semicolon()
        self.signed_integer = SignedInteger()
        self.symbols_for_defining = SymbolsForDefining()
        self.symbols_for_indicating = SymbolsForIndicating()
        self.variable_type = VariableType()
        self.whitespace = WhiteSpace()

    def _reset_all_states(self): 
        self.complete_counter = 0
        self.arithmatic.reset()
        self.assignment.reset()
        self.comma.reset()
        self.equal_comparision.reset()
        self.not_equal_comparision.reset()
        self.small_or_equal_comparision.reset()
        self.bigger_or_equal_comparision.reset()
        self.bigger_comparision.reset()
        self.smaller_comparision.reset()
        self.identifier.reset()
        self.keyword.reset()
        self.literal_string.reset()
        self.semicolon.reset()
        self.signed_integer.reset()
        self.symbols_for_defining.reset()
        self.symbols_for_indicating.reset()
        self.variable_type.reset()
        self.whitespace.reset()

    def process_acception(self, automata, i, line_num):
        transition_state, return_type_temp, return_value_temp = automata.accept(i, line_num)
        if transition_state == TransitionState.FAIL:
            automata.block()
        elif transition_state == TransitionState.COMPLETE:
            self.return_type, self.return_value = return_type_temp, return_value_temp
            self.complete_counter += 1

    def check_lexeme(self, i, line_num):
        self.process_acception(self.arithmatic, i, line_num)
        self.process_acception(self.comma, i, line_num)
        self.process_acception(self.whitespace, i, line_num)
        self.process_acception(self.equal_comparision, i, line_num)
        self.process_acception(self.assignment, i, line_num)
        

        if self.complete_counter == 1:
            self._reset_all_states()
            return True, self.return_type, self.return_value
        else:
            return False, None, None