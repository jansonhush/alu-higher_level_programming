# Python - Everything is object

These are my answers and scripts for the project about objects, identity, mutable and immutable types in Python.

## What's inside

- `0-answer.txt` to `18-answer.txt`: questions about `type`, `id`, `==` vs `is`, and how integers, strings and lists behave when assigned or passed to functions
- `19-copy_list.py`: function that returns a copy of a list
- `20-answer.txt` to `28-answer.txt`: questions about tuples, object identity and list concatenation (`+` vs `+=`)

## How to run

`19-copy_list.py` is meant to be imported from a main file:

```python
#!/usr/bin/python3
copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(copy_list(my_list) is my_list)
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
