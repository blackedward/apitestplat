from enum import Enum

from common.ValidUtil import ValidException


class FieldType(Enum):
    STRING = ("string", "string")
    STRING_ = ("str", "string")
    NUMBER = ("number", "number")
    NUMBER_ = ("num", "number")
    IN_DB = ("inDb", "inDb")
    NOT_IN_DB = ("notInDb", "notInDb")
    IN_DB_ = ("in_db", "inDb")
    NOT_IN_DB_ = ("not_in_db", "notInDb")
    CONST = ("const", "const")
    IN_ARRAY = ("inArray", "inArray")
    NOT_IN_ARRAY = ("notInArray", "notInArray")
    IN_ARRAY_ = ("in_array", "inArray")
    NOT_IN_ARRAY_ = ("not_in_array", "inArray")

    def __init__(self, type, value):
        self.type = type
        self.value = value

    @classmethod
    def get_field_type(cls, field_type):
        for enum in cls:
            if enum.type == field_type:
                return enum.value
        raise ValidException(f"unknown type: {field_type}")
