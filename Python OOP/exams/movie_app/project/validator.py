class Validator:
    @staticmethod
    def raise_error_if_name_is_empty_string(string, error_message):
        if not string:
            raise ValueError(error_message)

    @staticmethod
    def raise_error_if_num_is_below_restricted(num, num_limit, error_message):
        if num < num_limit:
            raise ValueError(error_message)