from enum import Enum


class Assertopr(Enum):
    EQ = 0, "=="
    LT = 1, "<"
    GT = 2, ">"
    LE = 3, "<="
    GE = 4, ">="
    SEQ = 5, 'eq'
    NE = 6, '!='
    RE = 7, 're'
    IS_NULL = 8, 'is_null'
    NOT_NULL = 9, 'not_null'
    COUNTAINS = 10, 'contains'
    IS_EMPTY = 11, 'is_empty'
    IS_NOT_EMPTY = 12, 'is_not_empty'
