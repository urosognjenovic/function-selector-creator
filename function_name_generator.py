import string
import random
from reserved_keywords import reserved_keywords

ascii_letters = string.ascii_letters
digits = string.digits
underscore = "_"
valid_first_function_name_character = ascii_letters + underscore
valid_function_name_characters = ascii_letters + digits + underscore

def generate_random_function_name(min_length, max_length):
    
    function_name_length = random.randint(
        min_length, max_length
    )
    first_character = random.choice(valid_first_function_name_character)
    other_characters = "".join(
        random.choices(
            valid_function_name_characters,
            k=function_name_length - 1,
        )
    )

    return first_character + other_characters


def function_name_is_reserved_keyword(function_name):
    if function_name in reserved_keywords:
        return True
    return False