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

-   unique: Check uniqueness of the value if the column in data
    -   data: Dataframe that used for validation
    -   targetColumn: Column name for validation
    -   fileName: Output text file name for error log
    -   filePath: Location for the output text file. E.g. ".\\Output\\" store error log in Output folder

#### Demo of some of the features:

```python
import pandas as pd
import validator
from validator import unique

df = pd.DataFrame({'A': [2, 3, 2], 'B': [4, 5, 6]})
unique(df, ['A', 'B'])
```
