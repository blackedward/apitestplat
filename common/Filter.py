import decimal

from common.ValidUtil import ValidUtil, ValidException


class Filter:

    def valid_for_string(self, allow_empty, min_len, max_len, allow_null):
        ValidUtil.not_null(allow_empty, "String field valid error, allowEmpty should not be null")
        ValidUtil.not_null(min_len, "String field valid error, minLen should not be null")
        ValidUtil.not_null(max_len, "String field valid error, maxLen should not be null")
        ValidUtil.is_greater_than_or_equals_zero(min_len,
                                                 "String field valid error, minLen must be greater than or equal to 0")
        ValidUtil.is_greater_than_or_equals_zero(max_len,
                                                 "String field valid error, maxLen must be greater than or equal to 0")
        ValidUtil.not_null(allow_null, "String field valid error, allowNull should not be null")
        if min_len > max_len:
            raise ValidException("String field valid error, maxLen should be greater than or equal to minLen")

    def valid_for_number(self, min_val, max_val, allow_null):
        ValidUtil.not_null(min_val, "Number field valid error, min should not be null")
        ValidUtil.not_null(max_val, "Number field valid error, max should not be null")
        ValidUtil.not_null(allow_null, "Number field valid error, allowNull should not be null")
        if min_val > max_val:
            raise ValidException("Number field valid error, max should be greater than or equal to min")

    # def valid_for_db_data(self, db_id, sql, element_type, allow_null):
    #     ValidUtil.not_null(db_id, "DbData field valid error, dbId should not be null")
    #     ValidUtil.not_null(sql, "DbData field valid error, sql should not be null")
    #     ValidUtil.not_null(element_type, "DbData field valid error, elementType should not be null")
    #     ValidUtil.not_null(allow_null, "DbData field valid error, allowNull should not be null")
    #     # 检查查询返回值类型是否在枚举范围
    #     ResultType.get_result_type(element_type)
    #     # 检查DbID是否存在于数据源管理表
    #     if self.db_service.find_db_by_id(db_id) is None:
    #         raise ValidException("DbData field valid error, dbId not found")
    #
    # def valid_for_const(self, constant, allow_null):
    #     ValidUtil.not_null(allow_null, "Const field valid error, allowNull should not be null")
    #     ValidUtil.not_null(constant, "Const field valid error, value should not be null")
    #
    # def valid_for_array_data(self, array_type, array_value, allow_null):
    #     ValidUtil.not_null(allow_null, "ArrayData field valid error, allowNull should not be null")
    #     ValidUtil.not_null(array_type, "ArrayData field valid error, elementType should not be null")
    #     ValidUtil.not_empty(array_value, "ArrayData field valid error, value should not be empty")
    #     ValidUtil.not_null(array_value, "ArrayData field valid error, value should not be null")
    #     # 检查数组元素类型是否在枚举范围
    #     ResultType.get_result_type(array_type)
