import pandas as pd
from .functions import check_type, check_column, log

# Unique validation
# data: Data source for validation
# targetColumn: Column name that requires for validation
# file: Invalid output text file name. E.g. ".\\Output\\Error_Log" store log in Output folder

def unique(data: pd.DataFrame, targetColumn: list, file = 'Error_Log'):
    # Validate parameter 
    check_type(pd.DataFrame, 'data', data, file)
    check_type(list, 'targetColumn', targetColumn, file)
    
    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        check_column(column, data, file)

        # Return duplicate rows
        df = data[data.duplicated([column], keep=False)]

        # Invalid data
        if not df.empty:
            invalid = True
            dfGroupBy = df.groupby(column)
            logContent += 'Column: ' + column
            logContent += '\nDuplicate value: \n'
            for name, group in dfGroupBy:
                logContent += '- {} ({} rows)\n'.format(name, len(group))
            logContent += '\n------------\n'

    if invalid:
        log(file, logContent)
        raise Exception('Duplicated value detected.')
