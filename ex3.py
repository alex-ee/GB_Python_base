import re

lst = ['зима','зима','весна','весна','весна','лето','лето','лето','осень','осень','осень','зима']

dct = {}
for i in range(1,13):
    dct[i] = lst[i-1]

ind = input('Введите номер месяца: ')

if ind.isdigit and int(ind) in range(1,13):
    print(f'по листу:\t{lst[int(ind)-1]}')
    print(f'по словарю:\t{dct[int(ind)]}')

else:
    print('введен неверный номер месяца')