class GrammarError(Exception):
    def __init__(self, line_idx, err_type) -> None:
        self.msg=f"Error on line {line_idx}: {err_type}"

    def __str__(self) -> str:
        return self.msg

class Grammar:
    def _check_variable_type(self, buffer: list, line_idx: int):
        token = ''.join(buffer)
        if token in ["int", "INT"]:
            return "VARIABLE", "INT"
        elif token in ["char", "CHAR"]:
            return "VARIABLE", "CHAR"
        return None, None

    def _check_signed_integer(self, buffer: list, line_idx: int):
        if buffer[0] == "0":
            return "SIGNED_INT", 0
    
        elif ord(buffer[0]) in range(ord('1'), ord('9')):
            for i in buffer:
                if i == "-" or i in range(ord('1'), ord('9')):
                    continue
                elif i in [" ", "\n", "\t", "\0", ";"]:
                    continue
                else:
                    raise GrammarError(line_idx, "Variable cannot start with number")
        else:
            return None, None

        return "SIGNED_INTEGER", int(''.join(buffer))

    def _check_white_space(self, buffer: list):
        for i in buffer:
            if i in [' ', '\n', '\t', '\0']:
                return "WHITESPACE", i
        return None, None


    def get_lexeme(self, line_idx: int, buffer: list):
        # 우선순위가 낮은 순서대로 저장 후 return
        signed_int, value = self._check_signed_integer(buffer, line_idx)
        if signed_int:
            return signed_int

        variable, value = self._check_variable_type(buffer, line_idx)
        if variable:
            return variable
        
        whiespace, value = self._check_white_space(buffer)
        if whiespace:
            return whiespace
     
