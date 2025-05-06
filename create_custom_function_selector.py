from web3 import Web3
import time
from exceptions import *
from input_validation import *
from function_name_generator import *

DEFAULT_FUNCTION_SELECTOR_LENGTH = 4


def create_custom_function_selector(
    min_function_name_length,
    max_function_name_length,
    target_selector_length=DEFAULT_FUNCTION_SELECTOR_LENGTH,
):
    print("Enter the target selector (without 0x):")
    target_selector = input()

    try:
        validate_target_selector_input(target_selector, target_selector_length)
    except WrongTargetSelectorLengthError as e:
        print(
            f"Wrong target selector length! You entered {e.actual_length} characters."
            f"The selector should be {target_selector_length} characters long."
        )
        return
    except UnsupportedCharacter as e:
        print(
            f"Unsupported character: '{e.character}'. Only hexadecimal digits (0-9 and a-f) are allowed."
        )
        return
    else:
        target_selector_with_prefix = "0x" + target_selector
        print("Your target selector is:", target_selector_with_prefix)

    print("Enter the desired parameter types separated with commas:")
    parameter_types = input()
    parameter_types_list = [
        parameter_type.strip() for parameter_type in parameter_types.split(",")
    ]

    validate_parameter_types_input(parameter_types_list)

    parameter_types_with_parentheses = "(" + ",".join(parameter_types_list) + ")"
    print(
        f"Your desired parameter types are (with parentheses): {parameter_types_with_parentheses}"
    )

    number_of_generated_signatures = 0

    start_time = time.time()
    while 1:
        number_of_generated_signatures += 1
        function_name = generate_random_function_name(
            min_function_name_length, max_function_name_length
        )
        function_signature = function_name + parameter_types_with_parentheses
        hash = Web3.keccak(text=function_signature).hex()
        function_selector = hash[:target_selector_length]

        if (
            function_selector == target_selector
            and not function_name_is_reserved_keyword(function_name)
        ):
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(
                f"Generated the desired function in {number_of_generated_signatures} attempts in {elapsed_time:.2f} seconds."
            )
            print("Function signature: ", function_signature)
            return
