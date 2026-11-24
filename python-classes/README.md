# Python - Classes and Objects

These are the scripts I wrote while learning how to define classes in Python: attributes, properties, validation and printing.

## What's inside

- `0-square.py`: an empty class `Square`
- `1-square.py`: `Square` with a private `size`
- `2-square.py`: `size` validation (`TypeError` / `ValueError`)
- `3-square.py`: adds the `area()` method
- `4-square.py`: `size` becomes a property with a getter and a setter
- `5-square.py`: adds `my_print()` to print the square with `#`
- `6-square.py`: adds a validated `position` used by `my_print()`

## How to run

Each class is meant to be imported from a main file:

```python
#!/usr/bin/python3
Square = __import__('6-square').Square

my_square = Square(3, (1, 1))
my_square.my_print()
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
