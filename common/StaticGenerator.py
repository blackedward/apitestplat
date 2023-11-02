from random import choice
from random import randint
import json

from common import RandomUtil
from common.Description import Description
from common.GeneratorAbstract import Generator


class StaticGenerator(Generator):  # 静态生成测试用例的类
    def __init__(self, filter, Description, dbService):
        self.filter = filter
        self.Description = Description
        self.dbService = dbService

    def gen_string(self, key, desc, allow_illegal, allow_empty, min_len, max_len, allow_null):  # 生成字段类型为String的用例

        result = []

        # 1. null
        if allow_null:
            result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_null(key, desc), None, key))
        else:
            result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_null(key, desc), None, key))

        # 2. empty
        if allow_empty:
            result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_empty(key, desc), "", key))
        else:
            result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_empty(key, desc), "", key))

        # 3. length
        # A. within length range
        random_legal_string = RandomUtil.randomLegalString(min_len, max_len)
        result.append(
            self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_length(key, desc, min_len, max_len),
                       random_legal_string, key))

        # B. exactly maximum length
        random_max = RandomUtil.randomLegalStringByLength(max_len)
        while random_max == random_legal_string:
            random_max = RandomUtil.randomLegalStringByLength(max_len)
        result.append(
            self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_equals_max_length(key, desc, max_len),
                       random_max, key))

        # C. exactly minimum length
        random_min = RandomUtil.randomLegalStringByLength(min_len)
        while random_min == random_legal_string or random_min == random_max:
            random_min = RandomUtil.randomLegalStringByLength(min_len)
        result.append(
            self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_equals_min_length(key, desc, min_len),
                       random_min, key))

        # D. exactly maximum length + 1
        result.append(
            self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_greater_length(key, desc, max_len, 1),
                       RandomUtil.randomLegalStringByLength(max_len + 1), key))

        # E. exactly minimum length - 1
        result.append(
            self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_less_length(key, desc, min_len, 1),
                       RandomUtil.randomLegalStringByLength(min_len - 1), key))

        if allow_illegal is not None:
            # 4. illegal characters
            if allow_illegal:
                result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS,
                                         Description.desc4_illegal_length(key, desc, min_len, max_len),
                                         RandomUtil.randomIllegalString(min_len, max_len), key))
            else:
                result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS,
                                         Description.desc4_illegal_length(key, desc, min_len, max_len),
                                         RandomUtil.randomIllegalString(min_len, max_len), key))

        return json.dumps(result)

    def gen_number(self, key, desc, min_val, max_val, allow_null):
        result = []

        # 1. null
        if allow_null:
            result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_null(key, desc), None, key))
        else:
            result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_null(key, desc), None, key))

        # 2. exactly maximum value
        result.append(
            self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_equals_max_size(key, desc, max_val), max_val,
                       key))

        if min_val < max_val:  # maximum value > minimum value, use values within the range as duplicate values
            # 3. exactly minimum value
            result.append(
                self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_equals_min_size(key, desc, min_val),
                           min_val, key))
            # find five values in the range that are not equal to the minimum value or maximum value
            for _ in range(5):
                big_decimal = RandomUtil.randomBigDecimal(min_val, max_val)
                if big_decimal == min_val and big_decimal == max_val:  # TODO: Maybe this is a bug,need to be tested
                    big_decimal = RandomUtil.randomBigDecimal(min_val, max_val)
                # 4. within the range of maximum and minimum values
            if big_decimal != min_val and big_decimal != max_val:
                result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS,
                                         Description.desc4_size(key, desc, min_val, max_val), big_decimal, key))

        # 5. exactly minimum value - step
        min_object = self.getLessThanMinNum(min_val)
        result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS,
                                 Description.desc4_less_size(key, desc, min_val, min_object['step']), min_object['num'],
                                 key))

        # 6. exactly maximum value + step
        max_object = self.getGreaterThanMaxNum(max_val)
        result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS,
                                 Description.desc4_greater_size(key, desc, max_val, max_object['step']),
                                 max_object['num'], key))

        return json.dumps(result)

    # def gen_in_db(self, key, desc, db_id, sql, element_type, allow_null):
    #     result = []
    #
    #     db = self.dbService.find_db_by_id(db_id)
    #     url = db['url']
    #     username = db['username']
    #     password = db['password']
    #
    #     result_type = ResultType.get_result_type(element_type)
    #
    #     # 0. null
    #     if allow_null:
    #         result.append(self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_null(key, desc), None, key))
    #     else:
    #         result.append(self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_null(key, desc), None, key))
    #
    #     rows = []
    #     if result_type == "string":
    #         rows = JdbcUtil.query_for_list(url, username, password, sql, str)
    #     elif result_type == "number":
    #         rows = JdbcUtil.query_for_list(url, username, password, sql, float)
    #     elif result_type == "integer":
    #         rows = JdbcUtil.query_for_list(url, username, password, sql, int)
    #
    #     if not rows:
    #         raise BusinessException("Query result is empty")
    #
    #     random_row = choice(rows)
    #
    #     # 1. valid equivalence class - in the table
    #     result.append(
    #         self.model(CaseType.VALID_EQUIVALENCE_CLASS, Description.desc4_in_db(key, desc), random_row[element_type],
    #                    key))
    #
    #     # 2. invalid equivalence class - not in the table
    #     invalid_value = None
    #     while invalid_value is None or invalid_value in [row[element_type] for row in rows]:
    #         invalid_value = self.random_legal_string(10, 20) if element_type == "string" else self.random_big_decimal(0,
    #                                                                                                                   100)
    #     result.append(
    #         self.model(CaseType.INVALID_EQUIVALENCE_CLASS, Description.desc4_not_in_db(key, desc), invalid_value, key))
    #
    #     return json.dumps(result)


class CaseType:
    VALID_EQUIVALENCE_CLASS = "VALID_EQUIVALENCE_CLASS"
    INVALID_EQUIVALENCE_CLASS = "INVALID_EQUIVALENCE_CLASS"
