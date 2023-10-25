from common.FiledType import FieldType
from common.ValidUtil import ValidException


class Inventory:
    def __init__(self, filter):
        self.filter = filter

    def gen_single_field(self, generator, key, desc, field_type, config):
        field_type = FieldType.get_field_type(field_type)
        allow_null = config.get("allowNull")

        if field_type == "string":
            allow_illegal = config.get("allowIllegal")
            allow_empty = config.get("allowEmpty")
            min_len = config.get("minLen")
            max_len = config.get("maxLen")
            self.filter.valid_for_string(allow_empty, min_len, max_len, allow_null)
            return generator.gen_string(key, desc, allow_illegal, allow_empty, min_len, max_len, allow_null)
        elif field_type == "number":
            min_val = config.get("min")
            max_val = config.get("max")
            self.filter.valid_for_number(min_val, max_val, allow_null)
            return generator.gen_number(key, desc, min_val, max_val, allow_null)
        elif field_type in ["inDb", "notInDb"]:
            db_id = config.get("dbId")
            sql = config.get("sql")
            element_type = config.get("elementType")
            self.filter.valid_for_db_data(db_id, sql, element_type, allow_null)
            if field_type == "inDb":
                return generator.gen_in_db(key, desc, db_id, sql, element_type, allow_null)
            else:
                return generator.gen_not_in_db(key, desc, db_id, sql, element_type, allow_null)
        elif field_type == "const":
            value = config.get("value")
            self.filter.valid_for_const(value, allow_null)
            return generator.gen_const(key, desc, value, allow_null)
        elif field_type in ["inArray", "notInArray"]:
            element_type = config.get("elementType")
            array_value = config.get("value")
            self.filter.valid_for_array_data(element_type, array_value, allow_null)
            if field_type == "inArray":
                return generator.gen_in_array(key, desc, array_value, element_type, allow_null)
            else:
                return generator.gen_not_in_array(key, desc, array_value, element_type, allow_null)
        else:
            raise ValidException("unknown type: " + field_type)
