# Python - More Classes and Objects

These are the scripts I wrote while learning more about classes in Python: properties, special methods, class attributes, static methods and class methods.

## What's inside

- `0-rectangle.py`: an empty class `Rectangle`
- `1-rectangle.py`: `Rectangle` with validated private `width` and `height`
- `2-rectangle.py`: adds `area()` and `perimeter()`
- `3-rectangle.py`: `str()` / `print()` draw the rectangle with `#`
- `4-rectangle.py`: `repr()` returns a string that `eval()` can turn back into a rectangle
- `5-rectangle.py`: prints `Bye rectangle...` when an instance is deleted
- `6-rectangle.py`: class attribute `number_of_instances`
- `7-rectangle.py`: class attribute `print_symbol` for the drawing character
- `8-rectangle.py`: static method `bigger_or_equal()`
- `9-rectangle.py`: class method `square()`

## How to run

Each class is meant to be imported from a main file:

```python
#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print(my_square)
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
