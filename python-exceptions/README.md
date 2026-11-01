# Python - Exceptions

These are the scripts I wrote while learning how to handle and raise exceptions in Python.

## What's inside

- `0-safe_print_list.py`: prints the first x elements of a list, safely
- `1-safe_print_integer.py`: prints an integer with `"{:d}".format()` and tells if it worked
- `2-safe_print_list_integers.py`: prints the integers among the first x elements of a list
- `3-safe_print_division.py`: divides two integers and prints the result in a `finally` block
- `4-list_division.py`: divides two lists element by element, handling the errors
- `5-raise_exception.py`: raises a `TypeError`
- `6-raise_exception_msg.py`: raises a `NameError` with a message

## How to run

Each function is meant to be imported from a main file:

```python
#!/usr/bin/python3
safe_print_division = __import__('3-safe_print_division').safe_print_division

print(safe_print_division(12, 0))
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
