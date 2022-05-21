from pydantic import BaseModel

class SLRGrammarData(BaseModel):
    lhs: str
    rhs_length: int
