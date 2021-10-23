class DivisionZero(Exception):
    pass

def mul(int1, int2):
    if int2 == 0:
        raise DivisionZero
    
    return int1 / int2

try:
    z = mul(10, 0)
    
except DivisionZero:
    print('деление на ноль')

