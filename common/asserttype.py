from enum import Enum


class AssertType(Enum):
    JSON = 0, 'json'
    HTML = 1, 'html'
    HEADER = 2, 'header'
    RESPONSE_CODE = 3, 'response_code'
    RUNTIME = 4, 'runtime'
