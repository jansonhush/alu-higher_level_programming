# Python - Import & modules

These are the scripts I wrote while learning how to import modules and use command-line arguments in Python.

## What's inside

- `0-add.py`: imports `add` from `add_0.py` and prints `1 + 2 = 3`
- `1-calculation.py`: imports `add`, `sub`, `mul` and `div` from `calculator_1.py` and prints each result
- `2-args.py`: prints the number of arguments and the list of arguments
- `3-infinite_add.py`: prints the sum of all arguments
- `4-hidden_discovery.py`: prints the names defined by the compiled module `hidden_4.pyc`
- `5-variable_load.py`: imports the variable `a` from `variable_load_5.py` and prints it

## Requirements

`add_0.py`, `calculator_1.py`, `variable_load_5.py` and `hidden_4.pyc` are provided with the project. `hidden_4.pyc` was compiled with Python 3.8, so task 4 must be run with Python 3.8.x.

## How to run

Make a script executable, then run it:

```bash
chmod u+x 2-args.py
./2-args.py Hello World
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
