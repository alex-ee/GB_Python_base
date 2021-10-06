def my_division(a, b):
    try:
        return int(a) / int(b)

    except ZeroDivisionError:
        return 'zero division error'
        
a, b = input('Введите два числа через пробел: ').split()

print(my_division(a, b))