# Validator

Validator is a Python package that contains validation function that use to validate data.

## Installation and updating

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Validator like below.
Rerun this command to check for and install updates .

```bash
pip install git+https://github.com/yongwahooi97/python-validator.git
```

## Usage

Features:

-   unique: Check uniqueness of the column of the data

#### Demo of some of the features:

```python
import validator
from validator import unique

df = pd.DataFrame({'A': [2, 3, 2], 'B': [4, 5, 6]})
unique(df, ['A', 'B'])
```
