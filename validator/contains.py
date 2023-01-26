import pandas as pd
from .functions import check_type, check_column, log

# Contains validation
# data: Data source for validation
# targetColumn: Column name that requires for validation 
# condition: Exact condition (Support multiple conditions by delimiter (,) E.g. A,B,C)
# file: Invalid output text file name. E.g. ".\\Output\\Error_Log" store log in Output folder

def contains(data: pd.DataFrame, targetColumn: list, condition: str, file = 'Error_Log'):
    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    check_type(str, 'condition', condition, file)

    invalid = False
    logContent = ''

    strConditions = condition.replace(',', '|')

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return rows that not contains 'condition'
        df = data[~data[column].map(str).str.contains(strConditions, na=False)]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that not contains `{}`: {} row(s)\n\n'.format(condition, len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Invalid contains detected.')
