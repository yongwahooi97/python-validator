import pandas as pd
from .log import log 

# Unique validation
# data: Data for validate
# targetColumn: Column that required for validation 
# fileName: Invalid output text file name
# filePath: Invalid output file location. E.g. .\\Output\\ 

def unique(data: pd.DataFrame, targetColumn: list, fileName = 'Unique_Error_Log', filePath = ''):
    # Validate parameter 
    if not isinstance(data, pd.DataFrame):
        raise TypeError('Invalid data type. Expected dataframe type.')
    if not isinstance(targetColumn, list):
        raise TypeError('Invalid data type. Expected list type.')
    
    invalid = False
    logContent = ''

    for column in targetColumn:
        # Check column name
        if column not in data.columns:
            raise Exception('Column not found: ' + column)

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
            logContent += '\n============\n'

    if invalid:
        log(fileName, filePath, logContent)
        raise Exception('Duplicated value detected.')
