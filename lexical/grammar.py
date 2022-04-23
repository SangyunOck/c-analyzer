from lexical.dfa import TransitionState
from lexical.automata.arithmatic import Arithmatic
from lexical.automata.comma import Comma
from lexical.automata.operator import Operator
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
    transition_state = None
    return_type = None
    return_value = None

    def __init__(self) -> None:
        self.complete_counter = 0
        self.arithmatic = Arithmatic()
        self.comma = Comma()
        self.operator = Operator()
        self.identifier = Identifier()
        self.keyword = Keyword()
        self.literal_string = LiteralString()
        self.semicolon = Semicolon()
        self.signed_integer = SignedInteger()
        self.symbols_for_defining = SymbolsForDefining()
        self.symbols_for_indicating = SymbolsForIndicating()
        self.variable_type = VariableType()
        self.whitespace = WhiteSpace()

    def reset_all_states(self):
        self.transition_state, self.return_type, self.return_value = TransitionState.FAIL, None, None
        self.arithmatic.reset()
        self.comma.reset()
        self.operator.reset()
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
        transition_state, return_type, return_value = automata.accept(i, line_num)

        if transition_state == TransitionState.FAIL:
            automata.block()
        
        if self.transition_state != TransitionState.COMPLETE:
            self.transition_state = transition_state
       
        if transition_state == TransitionState.COMPLETE:
            self.return_type, self.return_value = return_type, return_value

    def check_lexeme(self, i, line_num):
        # self.process_acception(self.whitespace, i, line_num)
        # self.process_acception(self.arithmatic, i, line_num)
        # self.process_acception(self.comma, i, line_num)
        # self.process_acception(self.operator, i, line_num)
        self.process_acception(self.literal_string, i, line_num)
        # self.process_acception(self.signed_integer, i, line_num)
        # self.process_acception(self.identifier, i, line_num)
        # self.process_acception(self.semicolon, i, line_num)
        
        
        
        
        if self.return_type and self.return_value:
            return self.transition_state, self.return_type, self.return_value
        
        return self.transition_state, None, None