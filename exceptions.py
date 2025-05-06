class WrongTargetSelectorLengthError(Exception):
    def __init__(self, actual_length):
        self.actual_length = actual_length
        super().__init__(f"Invalid selector length: {actual_length}")


class UnsupportedCharacter(Exception):
    def __init__(self, character):
        self.character = character
        super().__init__(f"Invalid character: {character}")


class InvalidParameterType(Exception):
    def __init__(self, actual_parameter_type):
        self.actual_parameter_type = actual_parameter_type
        super().__init__(f"Invalid parameter type: {actual_parameter_type}")
