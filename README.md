# Python Exercises

## Installing python3
Follow these [steps](https://docs.python-guide.org/starting/install3/osx/)

## Running the tests
We are using [`unittest`](https://docs.python.org/3/library/unittest.html) for our unit test framework.

To run all tests in both `linked_list` and `bignumber`:
```commandline
python3 -m unittest discover . "*.py"
```

To run tests in a just `linked_list` or `bignumber`:
```
python3 -m unittest <module>
```
