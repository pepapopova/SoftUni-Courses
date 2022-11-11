class Validator:
    @staticmethod
    def raise_if_len_is_less_than(obj, min_len, message):
        if len(obj) < min_len:
            raise ValueError(message)

    @staticmethod
    def raise_if_len_is_less_than_or_equal(num, min_num, message):
        if num <= min_num:
            raise ValueError(message)

    @staticmethod
    def raise_if_not_in_range(num, min_value, max_value, message):
        if num < min_value or num > max_value:
            raise ValueError(message)

    @staticmethod
    def raise_if_string_is_empty_or_whitespace(string, message):
        if string.strip() == '':
            raise ValueError(message)