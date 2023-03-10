import pandas as pd
from .functions import check_type, check_column, log

# Require validation
# data: Data source for validation
# targetColumn: Column name that requires for validation
# file: Invalid output text file name. E.g. ".\\Output\\Error_Log" store log in Output folder

def require(data: pd.DataFrame, targetColumn: list, file = 'Error_Log'):
    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    
    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return null or empty value rows
        df = data[data[column].isnull()]

        # Invalid data
        if not df.empty:
            invalid = True
            logContent += 'Column: ' + column
            logContent += '\nRow(s) that contains null or empty value: {} row(s)\n\n'.format(len(df))
            logContent += df.to_string(index=False)
            logContent += '\n\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Null or empty value detected.')
