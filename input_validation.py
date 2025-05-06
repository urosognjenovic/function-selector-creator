import string
from exceptions import *
from eth_abi.grammar import parse


def validate_target_selector_input(input, target_selector_length):
    if len(input) != target_selector_length:
        raise WrongTargetSelectorLengthError(len(input))

    for character in input:
        if character not in string.hexdigits:
            raise UnsupportedCharacter(character)


def validate_parameter_types_input(parameter_types_list):
    for parameter_type in parameter_types_list:
        try:
            parsed_parameter_type = parse(parameter_type)
            parsed_parameter_type.validate()
        except Exception as e:
            print(f"Error with the parameter type '{parameter_type}': {str(e)}")
