# Python - Input/Output

These are the scripts I wrote while learning how to read and write files, and how to serialize objects to JSON in Python.

## What's inside

- `0-read_file.py`: reads a text file and prints it
- `1-write_file.py`: writes a string to a file and returns the number of characters
- `2-append_write.py`: appends a string to a file and returns the number of characters
- `3-to_json_string.py`: returns the JSON representation of an object
- `4-from_json_string.py`: returns the object represented by a JSON string
- `5-save_to_json_file.py`: saves an object to a file as JSON
- `6-load_from_json_file.py`: loads an object from a JSON file
- `7-add_item.py`: script that adds its arguments to a list saved in `add_item.json`
- `8-class_to_json.py`: returns the dictionary description of an object
- `9-student.py`: class `Student` with `to_json()`
- `10-student.py`: `to_json()` with an attribute filter
- `11-student.py`: adds `reload_from_json()` (serialization and deserialization)
- `12-pascal_triangle.py`: returns Pascal's triangle of n rows

## How to run

Functions are meant to be imported from a main file, for example:

```python
#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

print(write_file("my_first_file.txt", "This School is so cool!\n"))
```

`7-add_item.py` can be run directly:

```bash
chmod u+x 7-add_item.py
./7-add_item.py Best School
```

## Author

Janson ([jansonhush](https://github.com/jansonhush))
