# Python - Inheritance

These are the scripts I wrote while learning about inheritance, `isinstance`/`issubclass`, and building classes on top of each other in Python.

## What's inside

- `0-lookup.py`: returns the attributes and methods of an object
- `1-my_list.py`: class `MyList` that inherits from `list` and can print itself sorted (tests in `tests/1-my_list.txt`)
- `2-is_same_class.py`: checks if an object is exactly an instance of a class
- `3-is_kind_of_class.py`: checks if an object is an instance of a class or of a subclass
- `4-inherits_from.py`: checks if an object is an instance of a subclass only
- `5-base_geometry.py`: empty class `BaseGeometry`
- `6-base_geometry.py`: adds an `area()` method that is not implemented
- `7-base_geometry.py`: adds `integer_validator()` (tests in `tests/7-base_geometry.txt`)
- `8-rectangle.py`: `Rectangle` inherits from `BaseGeometry` with private, validated sides
- `9-rectangle.py`: `Rectangle` with `area()` and a description
- `10-square.py`: `Square` inherits from `Rectangle`
- `11-square.py`: `Square` with its own description

## How to run the tests

From this directory:

```bash
python3 -m doctest -v ./tests/1-my_list.txt
python3 -m doctest -v ./tests/7-base_geometry.txt
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
