import pandas as pd

def unique(data: pd.DataFrame, targetColumn: list, fileName = 'Error_Log', filePath = '.\\Output\\'):
    # Validate parameter 
    if not isinstance(data, pd.DataFrame):
        raise TypeError('Invalid data type. Expected dataframe type.')
    if not isinstance(targetColumn, list):
        raise TypeError('Invalid data type. Expected list type.')
    
    invalid = False
    log = ''

    for column in targetColumn:
        # Check column name
        if column not in data.columns:
            raise Exception('Column not found: ' + column)

        df = data[data.duplicated([column], keep=False)]

        if not df.empty:
            invalid = True
            dfGroupBy = df.groupby(column)
            log += 'Column: ' + column
            log += '\nDuplicate value: \n'
            for name, group in dfGroupBy:
                log += '- {} ({} rows)\n'.format(name, len(group))
            log += '\n============\n'

    if invalid:
        # Write txt file
        f = open(filePath + fileName + '.txt', "w")
        print(log, file=f)
        f.close()
    print(log)
