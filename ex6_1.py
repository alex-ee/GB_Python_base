from itertools import count

for el in count(int(input('Введите начальное число: '))):
    if el > 50:
        break
    
    else:
        print(el)