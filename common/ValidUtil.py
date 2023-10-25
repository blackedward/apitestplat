class ValidUtil:

    @staticmethod
    def is_json_path(json_path):
        ValidUtil.not_null(json_path, "json path is null")
        ValidUtil.not_empty(json_path, "json path is empty")
        if not json_path.startswith("$"):
            raise ValidException(f"json path '{json_path}' syntax error")

    @staticmethod
    def is_xpath(xpath):
        ValidUtil.not_null(xpath, "xpath is null")
        ValidUtil.not_empty(xpath, "xpath is empty")
        if not xpath.startswith("\\"):
            raise ValidException(f"xpath '{xpath}' syntax error")

    @staticmethod
    def is_json_object(json_string, error_msg=None):
        try:
            # You would need to implement your JSON parsing logic here
            # For example, using the json module in Python
            pass
        except Exception as e:
            if error_msg is None:
                raise ValidException(f"json string error! {e}")
            else:
                raise ValidException(error_msg)

    @staticmethod
    def is_json_array(json_string, error_msg=None):
        try:
            # You would need to implement your JSON parsing logic here
            # For example, using the json module in Python
            pass
        except Exception as e:
            if error_msg is None:
                raise ValidException(f"json string error! {e}")
            else:
                raise ValidException(error_msg)

    @staticmethod
    def is_json(json_string, error_msg=None):
        is_object = True
        is_array = True
        msg = ""
        try:
            ValidUtil.is_json_object(json_string)
        except ValidException as e:
            is_object = False
            msg += str(e)
        try:
            ValidUtil.is_json_array(json_string)
        except ValidException as e:
            is_array = False
            msg += str(e)
        if not is_object and not is_array:
            if error_msg is None:
                raise ValidException(msg)
            else:
                raise ValidException(error_msg)

    @staticmethod
    def is_hash_map(json_string):
        try:
            # You would need to implement your JSON parsing logic here
            # For example, using the json module in Python
            pass
        except Exception as e:
            raise ValidException(f"json string error! {e}")

    @staticmethod
    def is_array_list(json_string):
        try:
            # You would need to implement your JSON parsing logic here
            # For example, using the json module in Python
            pass
        except Exception as e:
            raise ValidException(f"json string error! {e}")

    @staticmethod
    def is_object(json_string, clazz):
        try:
            # You would need to implement your JSON parsing logic here
            # For example, using the json module in Python
            pass
        except Exception as e:
            raise ValidException(f"json string error! {e}")

    @staticmethod
    def not_null(obj, msg):
        if obj is None:
            raise ValidException(msg)

    @staticmethod
    def not_empty(s, msg):
        ValidUtil.not_null(s, "ValidUtil.not_empty param 'String s' is null")
        if not s:
            raise ValidException(msg)

    @staticmethod
    def size(num, min, max, msg):
        if num > max or num < min:
            raise ValidException(msg)

    @staticmethod
    def length(s, min_length, max_length, msg):
        ValidUtil.not_null(s, "ValidUtil.length param 's' is null")
        s_len = len(s)
        if s_len > max_length or s_len < min_length:
            raise ValidException(msg)

    @staticmethod
    def is_word(s, error_msg=None):
        ValidUtil.not_null(s, "param is null")
        if not s.isalpha():
            if error_msg is None:
                raise ValidException("param must be English word")
            else:
                raise ValidException(error_msg)

    @staticmethod
    def is_word_underline(s, error_msg=None):
        ValidUtil.not_null(s, "param is null")
        if not s.isalpha() and not "_" in s:
            if error_msg is None:
                raise ValidException("param must be English word or underline")
            else:
                raise ValidException(error_msg)

    @staticmethod
    def is_greater_than_or_equals_zero(value, msg):
        if value < 0:
            raise ValidException(msg)


class ValidException(Exception):
    def __init__(self, message=None):
        super().__init__(message)
