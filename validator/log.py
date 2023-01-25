from datetime import datetime

def log(fileName, filePath, content):
     date = datetime.now()
     f = open(filePath + fileName + '.txt', "a")
     print('Date: '+ date.strftime("%d/%m/%y") + '\nTime: ' + date.strftime("%X"), file=f)
     print('\n============\n', file=f)
     print(content, file=f)
     f.close()