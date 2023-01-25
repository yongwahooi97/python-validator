from datetime import datetime

def check_type(dataType, key, value, file):
    if not isinstance(value, dataType):
        error_msg = 'Variable `' + str(key) + '` should be type ('
        error_msg += str(dataType) + ') but instead is type (' + str(type(value)) + ')'
        log(file, error_msg)
        raise TypeError(error_msg)

def log(file, content):
     date = datetime.now()
     f = open(file + '.txt', "a")
     print('\n========================\n', file=f)
     print('Date: '+ date.strftime("%d/%m/%y") + '\nTime: ' + date.strftime("%X"), file=f)
     print('\n------------\n', file=f)
     print(content, file=f)
     print('\n========================\n', file=f)
     f.close()