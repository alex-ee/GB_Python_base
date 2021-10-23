import re

class WrongInt(Exception):
    @staticmethod
    def check_int(arg):
        finded = re.findall('[0-9]+', arg)
        if not finded:
            raise WrongInt
        
        return finded

lst = []

st = ''
while not st:
    tmp = input('Введите число ("stop" для завершения): ')
    
    if tmp == 'stop':
        break
    try:
        lst.append(WrongInt.check_int(tmp))
        
    except WrongInt:
        print('текст запрещён')
    
print(lst)