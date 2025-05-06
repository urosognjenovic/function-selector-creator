## Intro

This repository allows you to create Solidity functions that accept specified parameters and generate the corresponding selector.

*The function selector is the first 4 bytes of the keccak256 hash of the function signature, and it is used to identify functions.*

## Features
- Custom function selector creation.
- Change the minimum and maximum length of the function name.
- Includes checks against the reserved keywords, supported characters, and parameter types.

## Getting started

```
git clone https://github.com/urosognjenovic/function-selector-creator
```

```
cd function-selector-creator
```

**For MacOS:**
```
python3 main.py
```

**For Windows:**
```
python main.py
```

or
```
py main.py
```

Input the target function selector (without the `0x` prefix) in the terminal.

Input the function parameter types.

## Customization

> [!IMPORTANT]
> The `parsimounious` library may cause problems with newer versions of Python.
To avoid these issues, install an older version of Python and run the script in a virtual environment.

`min_function_name_length` and `max_function_name_length` can be used to tune the function output. 

For testing purposes, one can changes the value of `target_selector_length`. Also, if this value is not passed to the `create_custom_function_selector` function, the function will use the default value (8 characters).

## Future upgrades

- Estimate number of guesses and required time
- Add option for user to make the function start with/end with/contain a certain string