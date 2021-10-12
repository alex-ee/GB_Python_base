from itertools import cycle

z = 0
for el in cycle([2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]):
    if z > 50:
        break
    
    else:
        print(el)
        z += 1