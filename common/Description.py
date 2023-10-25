class Description:
    def desc4_null(self, key, desc):
        return f"{desc}|{key}|为null"

    def desc4_not_null(self, key, desc):
        return f"{desc}|{key}|非null"

    def desc4_empty(self, key, desc):
        return f"{desc}|{key}|为空字符串"

    def desc4_not_empty(self, key, desc):
        return f"{desc}|{key}|非空字符串"

    def desc4_length(self, key, desc, min_len, max_len):
        return f"{desc}|{key}|长度在区间[{min_len},{max_len}]内"

    def desc4_illegal_length(self, key, desc, min_len, max_len):
        return f"{desc}|{key}|非法字符长度在区间[{min_len},{max_len}]内"

    def desc4_length_repeat(self, key, desc, min_len, max_len):
        return f"{desc}|{key}|长度在区间[{min_len},{max_len}]内-重复"

    def desc4_less_length(self, key, desc, min_len, step):
        return f"{desc}|{key}|长度为最小长度|{min_len}-{step}"

    def desc4_greater_length(self, key, desc, max_len, step):
        return f"{desc}|{key}|长度为最大长度|{max_len}+{step}"

    def desc4_equals_min_length(self, key, desc, min_len):
        return f"{desc}|{key}|长度恰好为最小长度|{min_len}"

    def desc4_equals_max_length(self, key, desc, max_len):
        return f"{desc}|{key}|长度恰好为最大长度|{max_len}"

    def desc4_size(self, key, desc, min_val, max_val):
        return f"{desc}|{key}|大小在区间[{min_val},{max_val}]内"

    def desc4_less_size(self, key, desc, min_val, step):
        return f"{desc}|{key}|为最小值|{min_val}-{step}"

    def desc4_greater_size(self, key, desc, max_val, step):
        return f"{desc}|{key}|为最大值|{max_val}+{step}"

    def desc4_equals_min_size(self, key, desc, min_val):
        return f"{desc}|{key}|恰好为最小值|{min_val}"

    def desc4_equals_max_size(self, key, desc, max_val):
        return f"{desc}|{key}|恰好为最大值|{max_val}"

    def desc4_in_db(self, key, desc):
        return f"{desc}|{key}|值存在于表内"

    def desc4_not_in_db(self, key, desc):
        return f"{desc}|{key}|值不存在于表内"

    def desc4_in_array(self, key, desc):
        return f"{desc}|{key}|值存在于数组内"

    def desc4_not_in_array(self, key, desc):
        return f"{desc}|{key}|值不存在于数组内"

    def desc4_const(self, key, desc, value):
        return f"{desc}|{key}|值为常量{value}"
